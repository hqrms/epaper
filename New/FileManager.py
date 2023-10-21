import os


def list_files_on_dir():
    directory = os.getcwd()

    items = os.listdir(directory)

    for item in items:
        full_path = os.path.join(directory, item)

        if os.path.isfile(full_path):
            print(f"Arquivo: {item}")
        elif os.path.isdir(full_path): 
            print(f"Diretório: {item}")


def save_file(file_name, content):
    with open(file_name, 'w') as arquivo:
        arquivo.write(content)

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        print(f"Conteúdo do arquivo '{file_name}':\n{content}")
        return content
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")


def create_file():
    with open("new", 'x') as arquivo:
        arquivo.write("")