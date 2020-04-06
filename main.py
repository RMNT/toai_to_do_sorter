import task
from todolist import todolist
import os
from os import system
import keyboard

def choices():
    print("\n1. Prideti uzduoti\n2. Perziureti uzduotis\n3. Redaguoti uzduoti\n4. Uzduociu skaicius\n5. Atlikta uzduotis\n6. Galimi veiksmai\n7. Konvertuoti i PDF\n8. Baigti darba (ir issaugoti)")

def wrongChoice():
    print("Tokio pasirinkimo nera")
    
def clear():
        system('clear')

def choose(x, taskList):
    switcher = {
        '1': taskList.addTask,
        '2': taskList.taskList,
        '3': taskList.editTask,
        '4': taskList.showTasksNumber,
        '5': taskList.delTask,
        '6': choices,
        '7': taskList.convertToPDF
    }
    return switcher.get(x, wrongChoice)()

if __name__ == "__main__":
    clear()
    taskList = todolist()
    if(os.path.isfile("tasks.txt")):
        taskList.fromFile()
    print("Uzduociu tvarkymo programa v1.0")
    print("Pasirinkite viena is veiksmu: ")
    
    while True:
        choices()
        x = input()
        if x == '8':
            taskList.toFile()
            clear()
            break
        choose(x, taskList)
        keyboard.wait('enter')
        clear()
        
#pip3 install keyboard