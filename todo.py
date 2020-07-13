#import pdb

def printTodoList(inputlist: list) -> type(None):
    for x in inputlist:
        print(f'{inputlist.index(x) + 1}. {x}\n')

def addTodoList() -> str:
    answer = input('What do you want to add to your todo list?\n')
    return answer

def delTodoList() -> str:
    answer = input('What do you want to delete to your todo list?\n')
    return answer

def initask():
    answer = input(
    """What would you like to add to your todo list?
    0. View list?
    1. Add to the todo list?
    2. Delete from todo list?
    3. Quit?\n"""
    )
    return answer

def main():
    todolist = []
#initask

    while True:
        answer = initask()

# answers
        if answer == '0':
            printTodoList(todolist)

        if answer == '1':
            added = addTodoList()
            todolist.append(added)

        if answer == '2':
            deleted = delTodoList()
            for x in todolist:
                if x.tolower() == deleted.tolower():
                    todolist.pop(index(x))
                    continue

        if answer == '3':
            return False

if __name__ == '__main__':
    exit(main())
