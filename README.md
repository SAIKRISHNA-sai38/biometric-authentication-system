# 🔐 Biometrics-Based Continuous Authentication System with Encryption

A Flask-based security system that combines biometric and behavioral
authentication to continuously verify a user's identity during a secure
banking session.

## 🚀 Key Features

### 👤 Multi-Factor Registration

The registration process collects multiple identity and behavioral
characteristics:

- Username and password
- Fingerprint image
- Facial biometric profile
- Typing rhythm
- Key dwell time
- Mouse movement behavior

### 🔑 Secure Login

The login process performs multiple verification stages:

1. Username and password verification
2. Fingerprint feature verification
3. Typing rhythm analysis
4. Key dwell-time analysis
5. Mouse movement analysis
6. Combined biometric scoring

### 📊 Behavioral Biometric Scoring

The system uses **Dynamic Time Warping (DTW)** to compare behavioral
patterns.

The scoring system combines:

- Typing intervals — 40%
- Key dwell times — 30%
- Mouse movement pattern — 20%
- Overall typing duration — 10%

A combined authentication score is calculated to determine whether the
current user matches the registered behavioral profile.

### 👁️ Continuous Face Authentication

After successful login, the system continuously monitors the user's face.

- Face verification runs periodically in the background.
- Unknown faces generate warnings.
- Multiple failed checks trigger automatic logout.
- The system displays the current authentication status.

### 🛡️ Intruder Detection

The system detects suspicious activity through:

- Failed password attempts
- Fingerprint mismatch
- Behavioral mismatch
- Unknown face detection
- Missing face detection
- Session timeout

Repeated authentication failures can automatically terminate the session.

### 🏦 Secure Banking Dashboard

The project includes a simulated banking environment with:

- Account balance
- Money transfers
- OTP verification
- Transaction history
- Beneficiary management
- Authentication status
- Security reports
- Intruder logs
- Fraud logs

### ⚠️ Fraud Monitoring

The system records suspicious transaction patterns such as:

- Large transfers
- Multiple transfers during a session

These events are recorded in fraud logs for monitoring.

## 🧰 Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- OpenCV
- NumPy
- face-api.js
- JSON
- Cryptography (Fernet)
- Dynamic Time Warping (DTW)
- SQLite/JSON-based local data storage

## Security Features

- Multi-factor biometric authentication
- Fernet symmetric encryption
- Facial recognition
- Fingerprint feature verification
- Behavioral biometric analysis
- Dynamic Time Warping
- OTP-based transaction verification
- Intruder detection
- Session monitoring
- Fraud monitoring
  
## 🔄 System Workflow

```text
                 ┌─────────────────────┐
                 │      REGISTER       │
                 └──────────┬──────────┘
                            │
            ┌───────────────┼────────────────┐
            │               │                │
            ▼               ▼                ▼
       Fingerprint       Face Profile    Behavioral Data
            │               │           ┌────┴─────┐
            │               │           │          │
            │               │        Typing      Mouse
            │               │        Rhythm     Movement
            └───────────────┼──────────────┬─────┘
                            ▼              │
                    Secure Data Storage   │
                            │              │
                            ▼              │
                         LOGIN ◄───────────┘
                            │
             ┌──────────────┼───────────────┐
             ▼              ▼               ▼
        Fingerprint     Behavioral       Password
        Verification    Verification    Verification
             │              │               │
             └──────────────┼───────────────┘
                            ▼
                   Authentication Score
                            │
                       ┌────┴────┐
                       │         │
                    PASS       FAIL
                       │         │
                       ▼         ▼
                  Banking     Reject
                  Dashboard
                       │
                       ▼
             Continuous Monitoring
                       │
             ┌─────────┼─────────┐
             ▼         ▼         ▼
            Face     Behavior   Session
          Monitoring   Check     Monitor
             │         │         │
             └─────────┼─────────┘
                       ▼
                Intruder Detection
                       │
                       ▼
                  Auto Logout
