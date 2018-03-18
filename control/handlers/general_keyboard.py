from gameutils.control import Keys
from threading import Thread, Lock
from pynput import keyboard

KEY_MAP = {
    Keys.ESC: keyboard.Key.esc,
    Keys.ENTER: keyboard.Key.enter,
    Keys.SPACE: keyboard.Key.space,
    Keys.UP: keyboard.Key.up,
    Keys.DOWN: keyboard.Key.down,
    Keys.RIGHT: keyboard.Key.right,
    Keys.LEFT: keyboard.Key.left
}

class GeneralKeyboard():

    def __init__(self):
        self.lock = Lock()
        self.th = Thread(target=self.listen, name="Keyboard handler", daemon=True)
        self.listener = None
        self.buffer_pressed = []
        self.__on_press_dict = {}

    def add_handle_press(self, key, callback, *args, **kwargs):
        key = KEY_MAP[key]
        to_call = {"call": callback, "args": args, "kwargs": kwargs}
        with self.lock:
            self.__on_press_dict[key] = {"call": callback, "args": args, "kwargs": kwargs}

    def __on_press(self, key):
        with self.lock:
            self.buffer_pressed.append(key)

    def handle(self):
        while self.buffer_pressed:
            event = self.buffer_pressed[0]
            if event in self.__on_press_dict:
                to_call = self.__on_press_dict[event]
                callback = to_call["call"]
                args = to_call["args"]
                kwargs = to_call["kwargs"]
                callback(*args, **kwargs)
            with self.lock:
                self.buffer_pressed.pop(0)

    def listen(self):
    # Collect events until released
        with keyboard.Listener(on_press=self.__on_press) as listener:
            self.listener = listener
            listener.join()

    def run(self):
        self.th.start()

    def stop(self):
        if self.listener:
            keyboard.Listener.stop(self.listener)
            self.listener = None
