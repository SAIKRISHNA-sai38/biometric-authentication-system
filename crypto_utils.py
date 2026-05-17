from cryptography.fernet import Fernet
import base64

# Generate key (run once and store it)
# key = Fernet.generate_key()
# print(key)

SECRET_KEY = b'keCCwINCVOiyDvMs7pcGhx4Dbe7OI6IZoThSjj80N2k='

cipher = Fernet(SECRET_KEY)

def encrypt_data(data):
    return cipher.encrypt(str(data).encode()).decode()

def decrypt_data(data):
    return eval(cipher.decrypt(data.encode()).decode())