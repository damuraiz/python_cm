import datetime, os, shutil

def log(message):
    with open("manager.log", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')} - {message}\n")
        print(message)

def get_list(only_folder=False):
    log(f"list (only_folder={only_folder})")
    result = os.listdir()
    if only_folder:
        result=[f for f in result if os.path.isdir(f)]
    log(f"list - {result}")
    return result

def create_file(name, text=None):
    log(f"create_file (name={name}, text={text})")
    with open(name, "w", encoding="utf-8") as f:
        if text:
            f.write(text)
        log(f"Файл {name} успешно создан")

def create_folder(name):
    log(f"create_folder (name={name})")
    try:
        os.mkdir(name)
    except FileExistsError:
        log(f"Папка {name} уже существует")
    else:
        log(f"Папка {name} создана")


def delete_file(name):
    log(f"delete_file (name={name})")
    try:
        if os.path.isdir(name):
            os.rmdir(name)
        else:
            os.remove(name)
    except FileNotFoundError:
        log(f"Файл/Папка {name} не найдена")
    else:
        log(f"Файл/Папка {name} успешно удалена")

def copy_file(name, new_name):
    log(f"copy_file (name={name}, new_name={new_name})")
    try:
        if os.path.isdir(name):
            shutil.copytree(name, new_name)
        else:
            shutil.copyfile(name, new_name)
    except FileNotFoundError:
        log(f"Файл/Папка {name} не найдена")
    except FileExistsError:
        log(f"Файл/Папка {name} уже существует")
    else:
        log(f"Файл/Папка {name} успешно скопирована с новым именем {new_name}")



if __name__ == "__main__":
#    print(get_list())
#    print(get_list(True))
    create_folder("test3")
    create_file("test1.txt")
    create_file("test2.txt", "Hello")
    copy_file("test3", "test4")
    copy_file("test2.txt", "test5.txt")
    delete_file("test3")
    delete_file("test4")
    delete_file("test1.txt")
    delete_file("test2.txt")
    delete_file("test5.txt")