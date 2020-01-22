import core, sys

core.log("Запущен консольный менеджер")

def read_help(file_name="help/general.txt"):
    with open(file_name, encoding="utf-8") as f:
        for line in f.readlines():
            print(line.replace("\n", ""))

def show_help(command=None):
    core.log(f"show_help(command={command}")
    try:
        if command:
            read_help(f"help/{command}.txt")
        else:
            read_help()
    except FileNotFoundError as e:
        core.log(f"Файл помощи для команды {command} не найден! {e}")

try:
    command = sys.argv[1]
    if command == "help":
        show_help()
    elif command == list:
        pass
    else:
        show_help()
except IndexError:
    show_help()
#show_help("mkfile")