import os

LOG_FILE = "keylogs.txt"


def write_log(entry: str):
    """Append a log entry to the log file."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)