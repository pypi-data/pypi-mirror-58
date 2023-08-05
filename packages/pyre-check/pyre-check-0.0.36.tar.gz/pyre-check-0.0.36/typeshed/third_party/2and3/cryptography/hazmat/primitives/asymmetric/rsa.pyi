from cryptography.hazmat.primitives.serialization import Encoding, KeySerializationEncryption, PrivateFormat, PublicFormat
from typing import Tuple

class RSAPrivateKey:
    def signer(self, padding, algorithm): ...
    def decrypt(self, ciphertext: bytes, padding) -> bytes: ...
    def public_key(self) -> RSAPublicKey: ...
    @property
    def key_size(self) -> int: ...
    def sign(self, data: bytes, padding, algorithm) -> bytes: ...

class RSAPrivateKeyWithSerialization(RSAPrivateKey):
    def private_numbers(self) -> RSAPrivateNumbers: ...
    def private_bytes(self, encoding: Encoding, format: PrivateFormat,
                      encryption_algorithm: KeySerializationEncryption) -> bytes: ...

class RSAPublicKey:
    def verifier(self, signature: bytes, padding, algorithm): ...
    def encrypt(self, plaintext: bytes, padding) -> bytes: ...
    @property
    def key_size(self) -> int: ...
    def public_numbers(self) -> RSAPublicNumbers: ...
    def public_bytes(self, encoding: Encoding, format: PublicFormat) -> bytes: ...
    def verify(self, signature: bytes, data: bytes, padding, algorithm) -> None: ...

RSAPublicKeyWithSerialization = RSAPublicKey

def generate_private_key(public_exponent: int, key_size: int, backend) -> RSAPrivateKeyWithSerialization: ...
def rsa_crt_iqmp(p: int, q: int) -> int: ...
def rsa_crt_dmp1(private_exponent: int, p: int) -> int: ...
def rsa_crt_dmq1(private_exponent: int, q: int) -> int: ...
def rsa_recover_prime_factors(n: int, e: int, d: int) -> Tuple[int, int]: ...

class RSAPrivateNumbers:
    def __init__(self, p: int, q: int, d: int, dmp1: int, dmq1: int, iqmp: int, public_numbers: RSAPublicNumbers) -> None: ...
    @property
    def p(self) -> int: ...
    @property
    def q(self) -> int: ...
    @property
    def d(self) -> int: ...
    @property
    def dmp1(self) -> int: ...
    @property
    def dmq1(self) -> int: ...
    @property
    def iqmp(self) -> int: ...
    @property
    def public_numbers(self) -> RSAPublicNumbers: ...
    def private_key(self, backend) -> RSAPrivateKey: ...

class RSAPublicNumbers:
    def __init__(self, e: int, n: int) -> None: ...
    @property
    def p(self) -> int: ...
    @property
    def q(self) -> int: ...
    def public_key(self, backend) -> RSAPublicKey: ...
