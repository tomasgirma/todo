def get_todos(file_path):
    with open(file_path, "r") as local_file:
        local_todos = local_file.readlines()
    return local_todos


def save_todos(todos, file_path):
    with open(file_path, "w") as local_file:
        local_file.writelines(todos)


def command():
    commands = input("Enter add, show, edit, complete or exit: ")
    commands.strip()
    return commands