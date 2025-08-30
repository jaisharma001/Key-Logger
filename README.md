🖥️ Python Keylogger (Educational Project)

A simple modular keylogger in Python that records keystrokes and also logs the active application/window where the typing happens.
This project is for learning purposes only — to understand event listeners, file handling, modular design, and OS-level APIs.

⚠️ Disclaimer: This tool is strictly for educational use on your own machine.
Misuse of keyloggers (e.g., stealing credentials, spying without consent) is illegal under computer misuse and cybercrime laws.

📂 Project Structure
keylogger_project/
│── main.py              # Entry point (starts the keylogger, emails logs after stop)
│── requirements.txt      # Dependencies
│── README.md             # Project documentation
│── .env                  # Environment variables (for email credentials)
│
├── logger/
│   ├── __init__.py
│   ├── keylogger.py      # Core keylogger logic
│   └── utils.py          # Helper functions (formatting, window detection, saving)
│
└── storage/
    ├── __init__.py
    ├── file_handler.py   # Save keystrokes to file
    └── email_handler.py  # Send logs via email


⚡ Features

Captures all keystrokes using pynput

Logs active window/app name whenever the user switches applications

Saves logs to a text file (keylogs.txt)

Modular structure for easy extension

Automatic email sending of logs after stopping (using .env credentials)

🚀 Usage

Create a .env file in the project root with your email credentials:

SENDER_EMAIL=your_email@gmail.com
APP_PASSWORD=your_app_password
RECEIVER_EMAIL=receiver_email@gmail.com


💡 For Gmail, you need to use an App Password, not your actual account password.

Run the keylogger:

python main.py


Keystrokes will be saved in keylogs.txt

Whenever the active window changes, the log will show:

=== Google Chrome ===
2025-08-22 12:10:01 - h
2025-08-22 12:10:02 - e
2025-08-22 12:10:03 - l
2025-08-22 12:10:04 - l
2025-08-22 12:10:05 - o


Press ESC to stop the program.
After stopping, logs will be emailed automatically.

📦 Dependencies

pynput
 — capture keystrokes

pywin32
 — get active window info (Windows only)

python-dotenv
 — load .env variables

Install all with:

pip install -r requirements.txt

📚 Learning Outcomes

Event listeners in Python (pynput)

File handling and logging

Detecting active applications/windows

Modular project design

Using .env files for safe credential management

Sending emails with smtplib

⚠️ Disclaimer

This project is intended only for educational purposes.
Do not use this software on devices or accounts without explicit permission.
The author is not responsible for any misuse.