# Biometrics-Based Continuous Authentication System with Encryption

## 📌 Project Overview

This project is a Flask-based security system that combines biometric authentication and behavioral biometrics for secure user verification.

The system uses:
- Fingerprint image upload
- Random biometric point extraction
- Typing pattern analysis
- Mouse movement tracking
- Cryptographic key generation
- Continuous authentication
- Intruder detection

The generated biometric key is used for secure authentication and encryption purposes.

---

## 🚀 Features

- 🔐 Fingerprint-based authentication
- ⌨️ Keystroke dynamics monitoring
- 🖱️ Mouse movement behavior tracking
- 🔑 Cryptographic key generation using SHA256
- 🔄 Continuous authentication after login
- 🚨 Intruder detection system
- 📝 Intruder logging
- 🔒 Encryption and decryption concept implementation

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- JavaScript
- JSON
- Cryptography (Fernet)
- Pillow (PIL)

---

## 📂 Project Structure

```plaintext
biometric_project/
│
├── app.py
├── crypto_utils.py
├── users.json
├── intruder_log.txt
│
├── static/
│
├── templates/
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
