from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import rsa

# Decrypt the encrypted_key to get the AES key for symmetric encryption/decryption.

with open ("riad_private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())
with open("encrypted_key", "rb") as f:
    key = f.read()
aes_key = rsa.decrypt(key,private_key)



# Verify the signature of the ciphered data sent and then decrypt using the AES key

with open("bakir_public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("signature", "rb") as f:
    signature = f.read()
with open("cipher.txt", "rb") as f:
    IV = f.read(16)
    ciphered_data = f.read()

print(rsa.verify(ciphered_data,signature,public_key))

cipher = AES.new(aes_key,AES.MODE_CBC,iv=IV)
original = unpad(cipher.decrypt(ciphered_data),AES.block_size)

with open("original.txt", "w") as f:
    f.write(original.decode())