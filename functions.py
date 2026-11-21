FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """ Читает текстовый файл и возвращает список дел."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Записывает список дел в текстовый файл."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Привет из функций.")
    print(get_todos())
