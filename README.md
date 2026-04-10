# 🔐 Password Strength Checker

A cybersecurity tool built in Python that analyzes password strength using multiple security checks including real-world breach database verification.

---

## 🚀 Features

- ✅ Basic strength checks (length, uppercase, lowercase, numbers, symbols)
- ✅ Common password detection (11,000+ wordlist)
- ✅ Entropy scoring using zxcvbn (same technology used by Dropbox)
- ✅ Real-time breach check via Have I Been Pwned API
- ✅ K-Anonymity privacy protection (password never sent to internet)
- ✅ Color coded terminal output (Red / Yellow / Green)
- ✅ 15 automated test cases

---

## 🛠️ Tech Stack

- Python 3.x
- requests
- colorama
- zxcvbn
- Have I Been Pwned API

---

## ⚙️ Installation

1. Clone the repository:

       git clone https://github.com/Sindudp/password-strength-checker.git

2. Navigate to the project folder:

       cd password-strength-checker

3. Install dependencies:

       pip install -r requirements.txt

---

## ▶️ Usage

    python main.py

Then enter any password when prompted.

---

## 🧪 Run Tests

    python tests/test_checker.py

---

## 📸 Sample Output

    === Password Strength Checker ===

    Enter a password to check: Hello@123456

    --- Password Analysis ---

    ✅ Not a commonly used password
    ✅ Good length
    ✅ Contains uppercase letter
    ✅ Contains lowercase letter
    ✅ Contains number
    ✅ Contains special character

    6/6 checks passed
    💪 Basic structure looks strong!

    --- Entropy Analysis ---
    🔐 Entropy Score: 3/4 — 🟢 Strong
    ⏱️  Estimated crack time: 5 months
    💬 Feedback: No suggestions

    --- Breach Database Check ---
    🔍 Checking breach database...
    ✅ This password was NOT found in any known data breach!

---

## 🔐 How Breach Check Works

This tool uses K-Anonymity to protect your privacy:
1. Password is hashed using SHA1
2. Only first 5 characters of hash are sent to API
3. Full password never leaves your device

---

## 👨‍💻 Author

- **Sindu D.P**
- GitHub: https://github.com/Sindudp

---

## 📄 License

This project is open source and available under the MIT License.