
def printTodoList(inputlist: list) -> type(None):
    for x in inputlist:
        print(x + "\n")

def addTodoList() -> type(None):
    answer = input('What do you want to add to your todo list?')


def main():
    todolist = []

    answer = input(
    """What would you like to add to your todo list?
    1. Add to the todo list?
    2. Delete from todo list?
    3. Quit?\n"""
    )

    if answer == 1:

    printTodoList(todolist)

if __name__ == '__main__':
    exit(main())
