#import pdb
from typing import IO

def printTodoList() -> type(None):
    readlist = open('todo.txt', 'r')
    for lines in readlist:
        print(f'{lines}')
    #for x in readlist:
        #print(f'{index(x) + 1}. x')

def addTodoList() -> type(None):
    answer = input('What do you want to add to your todo list?\n')
    todolist = open('todo.txt', mode='a', newline='')
    todolist.write(answer + '\n')
    return

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

#todofile write
#initask

    while True:
        answer = initask()

# answers
        if answer == '0':
            printTodoList()

        if answer == '1':
            addTodoList()

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
