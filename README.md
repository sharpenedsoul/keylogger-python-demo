# 🔐 Keylogger with Email Reporting (Educational Use Only)

This Python-based keylogger captures keyboard input and periodically sends it to an email address using SMTP over TLS. Created strictly for learning purposes to explore automation, secure communication, and system-level scripting.

---

## ⚠ Disclaimer

This tool is for *educational use only. Do not deploy or use this software without **explicit consent*. Unauthorized use may violate privacy laws.

---

## 🚀 Features

- Captures all keystrokes using the pynput library
- Logs regular and special keys
- Sends keystroke logs to your email using smtplib and ssl
- Configurable email credentials and send intervals
- Threaded timer for periodic email sending

---

## 🛠 Technologies Used

- Python 3.x
- pynput
- smtplib
- ssl
- threading

---

## ▶ Setup & Usage

### 1. Clone the repository
git clone https://github.com/yourusername/keylogger-python-demo.git
cd keylogger-python-demo

### 2. Install dependencies

pip install pynput

### 3. Configure your email

Enable 2FA in your Google account

Generate an App Password via Google App Passwords

Replace the sender_email, receiver_email, and password fields in keylogger.py


### 4. Run the script

python keylogger.py


---

### ⏱ Customization

You can adjust the email sending interval by modifying:

SEND_INTERVAL = 60  # in seconds


---

### 📄 Example Output

Keystrokes Logged:
a
b
[Backspace]
Shift


---

### 🧠 Skills Demonstrated

Email automation via SMTP

Secure communications using TLS/SSL

Keyboard event listening

Threading and scheduling

Ethical hacking awareness



---

### 👤 Author
### Ragi

### License
This project is open-source under the MIT License

### MIT License

Copyright (c) 2025 Ragi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files of this project, to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
