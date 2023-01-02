from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import rsa

# Open the file containing the key generated previously.

with open("aes_key","rb") as f:
    key = f.read()
cipher = AES.new(key,AES.MODE_CBC)

# Open the text file to be encrypted.

with open ("test.txt" , "rb") as f:
    message = f.read()

# Encrpyt the message and write it into a file.

ciphered_data = cipher.encrypt(pad(message,AES.block_size))
with open("cipher.txt","wb") as f:
    f.write(cipher.iv)
    f.write(ciphered_data)

# Sign the hashed version of the ciphered_data using my private key and write it into a file.

with open("bakir_private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())
signature = rsa.sign(ciphered_data,private_key,"SHA-256")
with open("signature","wb") as f:
    f.write(signature)

