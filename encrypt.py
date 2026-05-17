from cryptography.fernet import Fernet

# Generate key
key = Fernet.generate_key()

with open("key.key", "wb") as f:
    f.write(key)

cipher = Fernet(key)

# Read data
with open("data.json", "rb") as f:
    data = f.read()

# Encrypt
encrypted = cipher.encrypt(data)

with open("data.enc", "wb") as f:
    f.write(encrypted)

print("Data Encrypted Successfully")
