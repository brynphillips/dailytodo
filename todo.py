#import pdb

def printTodoList(inputlist: list) -> type(None):
    for x in inputlist:
        print(x + "\n")

def addTodoList() -> str:
    answer = input('What do you want to add to your todo list?\n')
    return answer

def delTodoList() -> str:
    answer = input('What do you want to delete to your todo list?\n')
    return answer

def main():
    todolist = []

    answer = input(
    """What would you like to add to your todo list?
    1. Add to the todo list?
    2. Delete from todo list?
    3. Quit?\n"""
    )


    if answer == "1":
        added = addTodoList()
        todolist.append(added)

    if answer == "2":
        deleted = delTodoList()

    printTodoList(todolist)

if __name__ == '__main__':
    exit(main())
