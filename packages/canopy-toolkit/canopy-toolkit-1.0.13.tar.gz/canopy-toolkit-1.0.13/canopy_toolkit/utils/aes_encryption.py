from base64 import b64encode, b64decode
from binascii import Error as Base64Error
from os.path import getsize as file_size
from re import sub as re_sub
from typing import Union, Optional

from Cryptodome.Cipher import AES
from Cryptodome.Hash import HMAC, SHA256, SHA512
from Cryptodome.Protocol.KDF import PBKDF2, HKDF
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad


class AesEncryption(object):
    """
    Encrypts data and files using AES CBC/CFB - 128/192/256 bits.

    The encryption and authentication keys
    are derived from the supplied key/password using HKDF/PBKDF2.
    The key can be set either with `set_master_key` or with `random_key_gen`.
    Encrypted data format: salt[16] + iv[16] + ciphertext[n] + mac[32].
    Ciphertext authenticity is verified with HMAC SHA256.

    Requires pycryptodome https://pycryptodome.readthedocs.io

    :ivar key_iterations: int The number of PBKDF2 iterations.
    :ivar base64: bool Accepts ans returns base64 encoded data.

    :param str mode: Optional, the AES mode (cbc or cfb).
    :param int size: Optional, the key size (128, 192 or 256).
    :raises ValueError: if the mode or size is invalid.
    """

    def __init__(self, mode: str = 'CBC', size: int = 256):
        """
        Initialize encryption utility.

        :param str mode: Optional, the AES mode (cbc or cfb).
        :param int size: Optional, the key size (128, 192 or 256).
        :raises ValueError: if the mode or size is invalid.
        """
        self._modes = {'CBC': AES.MODE_CBC, 'CFB': AES.MODE_CFB}
        self._sizes = (128, 192, 256)
        self._salt_len = 16
        self._iv_len = 16
        self._mac_len = 32
        self._mac_key_len = 32

        if mode.upper() not in self._modes:
            raise ValueError(mode + ' is not supported!')
        if size not in self._sizes:
            raise ValueError('Invalid key size!')
        self._mode = mode.upper()
        self._key_len = int(size / 8)
        self._master_key = None

        self.key_iterations = 20000
        self.base64 = True

    def encrypt(
            self, data: Union[str, bytes, bytearray], password: Optional[Union[str, bytes, bytearray]] = None
    ) -> bytes:
        """
        Encrypt data using the supplied password or a master key.

        The password is not required if a master key has been set -
        either with `random_key_gen` or with `set_master_key`.
        If a password is supplied, it will be used to create a key with PBKDF2.

        :param data: str or bytes or bytearray The plaintext.
        :param password: str or bytes or bytearray Optional, the password.
        :return: bytes Encrypted data (salt + iv + ciphertext + mac).
        """
        try:
            data = self._to_bytes(data)
            if self._mode == 'CBC':
                data = pad(data, AES.block_size)

            salt = self._random_bytes(self._salt_len)
            iv = self._random_bytes(self._iv_len)

            aes_key, mac_key = self._keys(salt, password)
            cipher = self._cipher(aes_key, iv)
            ciphertext = cipher.encrypt(data)
            mac = self._sign(iv + ciphertext, mac_key)

            encrypted = salt + iv + ciphertext + mac
            if self.base64:
                encrypted = b64encode(encrypted)
            return encrypted
        except (TypeError, ValueError) as e:
            self._error_handler(e)

    def decrypt(
            self, data: Union[str, bytes, bytearray], password: Optional[Union[str, bytes, bytearray]] = None
    ) -> bytes:
        """
        Decrypt data using the supplied password or a master key.

        The password is not required if a master key has been set -
        either with `random_key_gen` or with `set_master_key`.
        If a password is supplied, it will be used to create a key with PBKDF2.

        :param data: str or bytes or bytearray The ciphertext.
        :param password: str or bytes or bytearray Optional, the password.
        :return: bytes Plaintext.
        """
        try:
            data = self._to_bytes(data)
            data = b64decode(data) if self.base64 else data

            salt = data[:self._salt_len]
            iv = data[self._salt_len: self._salt_len + self._iv_len]
            ciphertext = data[self._salt_len + self._iv_len: -self._mac_len]
            mac = data[-self._mac_len:]

            aes_key, mac_key = self._keys(salt, password)
            self._verify(iv + ciphertext, mac, mac_key)

            cipher = self._cipher(aes_key, iv)
            plaintext = cipher.decrypt(ciphertext)
            if self._mode == 'CBC':
                plaintext = unpad(plaintext, AES.block_size)
            return plaintext
        except (TypeError, ValueError, Base64Error) as e:
            self._error_handler(e)

    def encrypt_file(
            self, path: str, password: Optional[Union[str, bytes, bytearray]] = None
    ) -> str:
        """
        Encrypt files using the supplied password or a master key.

        The password is not required if a master key has been set -
        either with `random_key_gen` or with `set_master_key`.
        If a password is supplied, it will be used to create a key with PBKDF2.
        The original file is not modified; a new encrypted file is created.

        :param str path: The file path.
        :param password: str or bytes Optional, the password.
        :return: str The new file path.
        """
        try:
            salt = self._random_bytes(self._salt_len)
            iv = self._random_bytes(self._iv_len)

            aes_key, mac_key = self._keys(salt, password)
            cipher = self._cipher(aes_key, iv)
            hmac = HMAC.new(mac_key, digestmod=SHA256)
            new_path = path + '.enc'

            with open(new_path, 'wb') as f:
                f.write(salt + iv)
                hmac.update(iv)

                for chunk, is_last in self._file_chunks(path):
                    if self._mode == 'CBC' and is_last:
                        chunk = pad(chunk, AES.block_size)
                    data = cipher.encrypt(chunk)
                    f.write(data)
                    hmac.update(data)

                f.write(hmac.digest())
            return new_path
        except (TypeError, ValueError, IOError) as e:
            self._error_handler(e)

    def decrypt_file(self, path: str, password: Optional[Union[str, bytes, bytearray]] = None) -> str:
        """
        Decrypt files using the supplied password or a master key.

        The password is not required if a master key has been set -
        either with `random_key_gen` or with `set_master_key`.
        If a password is supplied, it will be used to create a key with PBKDF2.
        The original file is not modified; a new decrypted file is created.

        :param str path: The file path.
        :param password: str or bytes Optional, the password.
        :return: str The new file path.
        """
        try:
            with open(path, 'rb') as f:
                salt = f.read(self._salt_len)
                iv = f.read(self._iv_len)
                f.seek(file_size(path) - self._mac_len)
                mac = f.read(self._mac_len)

            aes_key, mac_key = self._keys(salt, password)
            self._verify_file(path, mac, mac_key)
            cipher = self._cipher(aes_key, iv)
            new_path = re_sub(r'\.enc$', '.dec', path)

            with open(new_path, 'wb') as f:
                chunks = self._file_chunks(
                    path, self._salt_len + self._iv_len, self._mac_len
                )
                for chunk, is_last in chunks:
                    data = cipher.decrypt(chunk)

                    if self._mode == 'CBC' and is_last:
                        data = unpad(data, AES.block_size)
                    f.write(data)
            return new_path
        except (TypeError, ValueError, IOError) as e:
            self._error_handler(e)

    def set_master_key(self, key: Union[str, bytes, bytearray], raw: bool = False):
        """
        Set a new master key.

        This key will be used to create the encryption and authentication keys.

        :param bool raw:
        :param key: str or bytes or bytearray The new master key.
        """
        try:
            if not raw:
                key = b64decode(key)
            self._master_key = self._to_bytes(key)
        except (TypeError, Base64Error) as e:
            self._error_handler(e)

    def get_master_key(self, raw: bool = False) -> bytes:
        """
        Return the master key (or `None` if the key is not set).

        :param bool raw: Optional, returns raw bytes; not base64-encoded.
        :return: bytes The master key.
        """
        if self._master_key is None:
            self._error_handler(ValueError('The key is not set!'))
        elif not raw:
            return b64encode(self._master_key)
        else:
            return self._master_key

    def random_key_gen(self, key_len: int = 32, raw: bool = False) -> bytes:
        """
        Generate a new random key.

        This key will be used to create the encryption and authentication keys.

        :param int key_len: length of the key
        :param bool raw:  Optional, returns raw bytes; not base64-encoded.
        :return: bytes The new master key.
        """
        self._master_key = self._random_bytes(key_len)
        if not raw:
            return b64encode(self._master_key)
        return self._master_key

    def _keys(self, salt: bytes, password: str):
        """
        Derive encryption and authentication keys from a key or password.

        If the password is not null, it will be used to create the keys.

        :raises ValueError: if neither the key or password is set.
        """
        if password is not None:
            dkey = PBKDF2(
                password, salt, self._key_len + self._mac_key_len,
                self.key_iterations, hmac_hash_module=SHA512
            )
        elif self._master_key is not None:
            dkey = HKDF(
                self._master_key, self._key_len + self._mac_key_len,
                salt, SHA256
            )
        else:
            raise ValueError('No password or key specified!')
        return dkey[:self._key_len], dkey[self._key_len:]

    @staticmethod
    def _random_bytes(size):
        """Create random bytes; used for IV, salt and key generation."""
        return get_random_bytes(size)

    def _cipher(self, key, iv):
        """Create AES object; used for encryption / decryption."""
        return AES.new(key, self._modes[self._mode], IV=iv)

    def _sign(self, ciphertext, key):
        """Compute the MAC of ciphertext; used for authentication."""
        hmac = HMAC.new(key, ciphertext, digestmod=SHA256)
        return hmac.digest()

    def _sign_file(self, path, key):
        """Compute the MAC of ciphertext; used for authentication."""
        hmac = HMAC.new(key, digestmod=SHA256)
        for data, _ in self._file_chunks(path, self._salt_len):
            hmac.update(data)
        return hmac.digest()

    @staticmethod
    def _verify(data, mac, key):
        """
        Verify the authenticity of ciphertext.

        :raises ValueError: if the MAC is invalid.
        """
        hmac = HMAC.new(key, data, digestmod=SHA256)
        hmac.verify(mac)

    def _verify_file(self, path, mac, key):
        """
        Verify the authenticity of ciphertext.

        :raises ValueError: if the MAC is invalid.
        """
        hmac = HMAC.new(key, digestmod=SHA256)
        beg, end = self._salt_len, self._mac_len

        for chunk, _ in self._file_chunks(path, beg, end):
            hmac.update(chunk)
        hmac.verify(mac)

    @staticmethod
    def _error_handler(exception):
        """Handle exceptions (prints the exception by default)."""
        raise exception

    @staticmethod
    def _file_chunks(path, beg=0, end=0):
        """
        Read file and yields chunks of data.

        The chunk size should be a multiple of 16 in CBC mode.
        """
        size = 1024
        end = file_size(path) - end

        with open(path, 'rb') as f:
            pos = (len(f.read(beg)))
            while pos < end:
                size = size if end - pos > size else end - pos
                data = f.read(size)
                pos += len(data)

                yield (data, pos == end)

    @staticmethod
    def _to_bytes(data, encoding='utf-8'):
        """Convert unicode strings and byte arrays to byte strings."""
        if hasattr(data, 'encode'):
            data = bytes(data, encoding)
        if type(data) is bytearray:
            data = bytes(data)
        return data
