from pynput import keyboard

arrow_list = ["Key.left", "Key.right", "Key.up", "Key.down"]

def read_file(file_name):
    with open(file_name, 'r') as file:
        conteudo = file.read()
        return conteudo

word = read_file("text.txt")
cursor = len(word)

def on_press(key):
    global word
    global cursor
    
    try:
        word = word[:cursor] + key.char + word[cursor:]
        cursor += 1
        print(word)
    except AttributeError:
        print(key, cursor)
        if str(key) == "Key.space":
            word = word[:cursor] + " " + word[cursor:]
            cursor += 1
        if str(key) == "Key.ctrl":
            save_text_to_file(word)
        if str(key) == "Key.left" and cursor > 0:
            cursor -= 1
        if str(key) == "Key.right" and cursor <= len(word):
            cursor += 1

def save_text_to_file(text):
    try:
        with open("text.txt", 'w') as file:
            file.write(text)
        file.close()
    except Exception as e:
        print("Ocorreu um erro ao escrever o arquivo:", e)


def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

