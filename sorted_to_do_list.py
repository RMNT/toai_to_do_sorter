import task
from todolist import todolist
import os.path

def choices():
    print("\n1. Prideti uzduoti\n2. Perziureti uzduotis\n3. Redaguoti uzduoti\n4. Uzduociu skaicius\n5. Atlikta uzduotis\n6. Galimi veiksmai\n7. Baigti darba")

def choose(x, taskList):
    switcher = {
        '1': taskList.addTask,
        '2': taskList.taskList,
        '3': taskList.editTask,
        '5': taskList.showTasksNumber,
        '6': taskList.delTask,
        '7': choices
    }
    return switcher.get(x)()

if __name__ == "__main__":
    taskList = todolist()
    #f = open("tasks.txt", "w")
    if(os.path.isfile("tasks.txt")):
        taskList.fromFile()
    print("Uzduociu tvarkymo programa v1.0")
    print("Pasirinkite viena is veiksmu: ")
    choices()
    
    while (1):
        x = input()
        if(x == '7'):
            taskList.toFile()
            break
        choose(x, taskList)
        #   keletas imanomu sarasu
        #uztiktinti pavadinimo unikaluma
        #   integracija su google calender