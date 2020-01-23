import core, sys

core.log("Запущен консольный менеджер")


def read_help(file_name="help/general.txt"):
    with open(file_name, encoding="utf-8") as f:
        for line in f.readlines():
            print(line.replace("\n", ""))


def show_help(command=None):
    core.log(f"show_help(command={command})")
    try:
        if command:
            read_help(f"help/{command}.txt")
        else:
            read_help()
    except FileNotFoundError as e:
        core.log(f"Файл помощи для команды {command} не найден! {e}")


try:
    command = sys.argv[1]
except IndexError:
    show_help()
else:
    if command == "help":
        show_help()
    elif command == "list":
        if len(sys.argv) > 2:
            if sys.argv[2] == 'od' or sys.argv[2] == 'only_directory':
                for file in core.get_list(True):
                    print(file)
            else:
                show_help(command)
        else:
            for file in core.get_list():
                print(file)
    elif command == "copy":
        if len(sys.argv) > 3:
            core.copy_file(sys.argv[2], sys.argv[3])
        else:
            show_help(command)
    elif command == "delete":
        if len(sys.argv) > 2 and sys.argv[2]!='help':
            core.delete_file(sys.argv[2])
        else:
            show_help(command)
    elif command == "mkdir":
        if len(sys.argv) > 2:
            if sys.argv[2]!='help':
                core.create_folder(sys.argv[2])
            else:
                show_help(command)
    elif command == "mkfile":
        if len(sys.argv) > 2:
            if sys.argv[2]!='help':
                if len(sys.argv) > 3:
                    core.create_file(sys.argv[2], sys.argv[3])
                else:
                    core.create_file(sys.argv[2])
            else:
                show_help(command)
    else:
        show_help()


