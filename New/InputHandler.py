import subprocess
from FileManager import save_file, read_file, list_files_on_dir
import re
from DisplayManager import DisplayManager

class InputHandler():
    def __init__(self):

        self.interface_mode = 1
        self.file = read_file("txt.txt")
        self.cursor = len(self.file)
        self.display_manager = DisplayManager()

        self.arrow_keys = {
            "Key.right": 1,
            "Key.left": -1,
            "Key.up": len(self.file) * -1,
            "Key.down": len(self.file) * 1,
        }

    def process_key_press(self, key):
        if self.interface_mode == 1:
            self.edit_file(self.file, key)
            self.display_manager.draw_text([0,0], self.file)


    def process_key_release(self, key):
        if str(key) == "Key.esc":
            save_file("txt.txt", self.file)
            return False
        if str(key) == "Key.alt":
            self.interface_mode *= -1
            print("Interface Mode Changed", self.interface_mode)

    def move_cursor(self, value):
        self.cursor += value
        if self.cursor < 0:
            self.cursor = 0
        if self.cursor > len(self.file) *2:
            self.cursor = len(self.file) *2

        print(self.cursor)

    def edit_file(self, file, key):
        try:
            self.file = self.file[:self.cursor] + str(key.char)
            self.move_cursor(1)
        except:   
                if str(key) == "Key.backspace":
                        self.file = file[:-1]      
                elif str(key) == "Key.enter":
                        self.file = self.file[:self.cursor] +'\n'       
                elif str(key) == "Key.space":
                        self.file = self.file[:self.cursor] + ' '       
                elif str(key) in self.arrow_keys:
                        self.move_cursor(self.arrow_keys[str(key)])


    def run_terminal_command(self):
        command = "ls"
        output = subprocess.check_output(command, shell=True)

        print(output.decode('utf-8')) 
