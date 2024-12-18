import function
import time

now = time.strftime("%b %d %H:%M")
print("now its ", now)

while True:
    input_command = function.command()
    if input_command.startswith('add'):

        todos = function.get_todos("todos.txt")

        new_todo = input_command[4:] + "\n"

        todos.append(new_todo)

        function.save_todos("todos.txt")

    elif input_command.startswith('show'):

        todos = function.get_todos("todos.txt")

        for i, items in enumerate(todos):
            items = items.strip('\n')
            print(f"{i + 1}.{items}")
    elif input_command.startswith('edit'):

        todos = function.get_todos("todos.txt")
        numb = int(input_command[5:])
        numb -= 1
        edited_todo = input("Enter new todo: ") + "\n"

        todos[numb] = edited_todo

        function.save_todos("todos.txt")
    elif input_command.startswith('complete'):
        try:
            todo_to_complete = int(input_command[9:])
            todo_to_complete -= 1

            todos = function.get_todos("todos.txt")
            completed_todo = todos[todo_to_complete].strip('\n')

            todos.pop(todo_to_complete)
            print(f"Todo {completed_todo} has been completed")

            function.save_todos("todos.txt")
        except ValueError:
            print("your command is not valid")
            continue

    elif 'exit' in input_command:
        break

print("Bye!")
