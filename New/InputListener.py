from pynput.keyboard import Key, Listener
from InputHandler import InputHandler

class InputListener():
    def __init__(self):
        self.input_handler = InputHandler()
        self.init_listener()

    def init_listener(self):
        with Listener(on_press=self.on_key_press, 
                                on_release=self.on_key_release
                                ) as listener:
                listener.join()

    def on_key_press(self, key):
        self.input_handler.process_key_press(key)

    def on_key_release(self, key):
       return self.input_handler.process_key_release(key)

    def stop_listener(self):
        self.listener.stop()



teste = InputListener()