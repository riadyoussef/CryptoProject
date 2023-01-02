import rsa

# Generate RSA Public and Private Keys and write them into files.

public_key, private_key = rsa.newkeys(2048)
with open("riad_public.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))
with open("riad_private.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))



