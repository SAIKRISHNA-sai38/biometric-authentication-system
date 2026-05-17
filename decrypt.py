from cryptography.fernet import Fernet

# Load key
with open("key.key", "rb") as f:
    key = f.read()

cipher = Fernet(key)

# Read encrypted data
with open("data.enc", "rb") as f:
    encrypted = f.read()

# Decrypt
decrypted = cipher.decrypt(encrypted)

print("Decrypted Data:", decrypted)
