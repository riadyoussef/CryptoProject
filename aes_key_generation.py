from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import rsa

# Generate AES Key and write it into a file.

salt = get_random_bytes(32)
password = "P@$$w0rd123"
key = PBKDF2(password, salt, dkLen=32)

with open ("aes_key", "wb") as f:
    f.write(key)

# Encrypt AES key with recipient public key and write it into a file.

with open ("riad_public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

encrypted_key = rsa.encrypt(key,public_key)

with open("encrypted_key", "wb") as f:
    f.write(encrypted_key)

