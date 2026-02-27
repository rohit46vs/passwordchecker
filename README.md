# 🔐 Password Strength Checker

A beginner-friendly cybersecurity project that analyzes the strength of passwords and gives detailed feedback — built with Python.

---

## 📁 Project Structure

```
Proje/
├── password_checker.py   # Main program file
└── README.md             # This file
```

---

## ⚙️ Requirements

- Python 3.x installed on your system
- No external libraries needed — uses built-in Python modules only!

---

## 🚀 How to Run

### Step 1 — Open the project in VS Code
- Open VS Code
- Go to **File → Open Folder** and select your `Proje` folder

### Step 2 — Open the terminal
- Press `Ctrl + `` ` `` ` or go to **Terminal → New Terminal**

### Step 3 — Run the program
```bash
python password_checker.py
```

> If that doesn't work, try:
> ```bash
> py password_checker.py
> ```
> or
> ```bash
> python3 password_checker.py
> ```

---

## 🖥️ How to Use

Once the program runs, you'll see a menu:

```
=============================================
   🔐 PASSWORD STRENGTH CHECKER
=============================================
  Built for learning cybersecurity basics!
=============================================

Options:
  [1] Check a password        ← shows password as you type
  [2] Check password (hidden) ← hides password while typing
  [3] Exit
```

- Press `1` to check a password (visible)
- Press `2` to check a password (hidden input — more secure)
- Press `3` to exit

### Example Output:
```
=============================================
  PASSWORD STRENGTH: 🟢 STRONG
  SCORE: 7/8
=============================================

📋 Feedback:
   ✅ Great length (12+ characters).
   ✅ Contains lowercase letters.
   ✅ Contains uppercase letters.
   ✅ Contains numbers.
   ✅ Contains special characters — nice!

  Strength Bar: [████████░░]
```

---

## 🔍 What It Checks

| Check | Details |
|---|---|
| **Length** | Short (<8), Decent (8-11), Great (12+) |
| **Lowercase letters** | a-z |
| **Uppercase letters** | A-Z |
| **Numbers** | 0-9 |
| **Special characters** | !@#$%^&* etc. |
| **Common passwords** | Checks against 20 common weak passwords |
| **Repeated characters** | e.g. `aaa`, `111` |
| **Sequential patterns** | e.g. `abc`, `123`, `qwerty` |

---

## 📊 Scoring System

| Score | Strength |
|---|---|
| 0 – 2 | 🔴 Weak |
| 3 – 4 | 🟠 Fair |
| 5 – 6 | 🟡 Moderate |
| 7 | 🟢 Strong |
| 8 | 💪 Very Strong |

---

## 🧠 What You Learn From This Project

- Using **regular expressions (regex)** to detect patterns — a core cybersecurity skill
- Understanding what makes passwords **weak or strong**
- Basic **Python programming** — functions, loops, conditionals
- How attackers exploit **common and predictable passwords**

---

## 🛡️ Security Note

> This tool is for **educational purposes only**. Never share your real passwords with any tool online. This program runs **100% locally** on your machine — nothing is sent anywhere.

---

## 🗺️ What's Next?

This is **Project 1** of a cybersecurity learning series. Coming up next:

- 📌 **Project 2** — Caesar Cipher / Encryption Tool
- 📌 **Project 3** — Port Scanner
- 📌 **Project 4** — Network Packet Analyzer
- 📌 **Project 5** — Web Vulnerability Scanner
- 📌 **Project 6** — Honeypot
- 📌 **Project 7** — Log Analyzer

---

## 👨‍💻 Author

Built by a cybersecurity enthusiast learning one project at a time. 🚀
