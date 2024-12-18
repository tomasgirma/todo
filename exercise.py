def get_todos(file_path):
    with open(file_path, "r") as local_file:
        local_todos = local_file.readlines()
    return local_todos


def save_todos(file_path):
    with open(file_path, "w") as local_file:
        local_file.writelines(todos)


def command():
    commands = input("Enter add, show, edit, complete or exit: ")
    commands.strip()
    return commands


while True:
    input_command = command()
    if input_command.startswith('add'):

        todos = get_todos("todos.txt")

        new_todo = input_command[4:] + "\n"

        todos.append(new_todo)

        save_todos("todos.txt")

    elif input_command.startswith('show'):

        todos = get_todos("todos.txt")

        for i, items in enumerate(todos):
            items = items.strip('\n')
            print(f"{i + 1}.{items}")
    elif input_command.startswith('edit'):

        todos = get_todos("todos.txt")
        numb = int(input_command[5:])
        numb -= 1
        edited_todo = input("Enter new todo: ") + "\n"

        todos[numb] = edited_todo

        save_todos("todos.txt")
    elif input_command.startswith('complete'):
        try:
            todo_to_complete = int(input_command[9:])
            todo_to_complete -= 1

            todos = get_todos("todos.txt")
            completed_todo = todos[todo_to_complete].strip('\n')

            todos.pop(todo_to_complete)
            print(f"Todo {completed_todo} has been completed")

            save_todos("todos.txt")
        except ValueError:
            print("your command is not valid")
            continue

    elif 'exit' in input_command:
        break

print("Bye!")
