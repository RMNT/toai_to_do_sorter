from task import task
import re
from datetime import date as dt, timedelta, datetime

class todolist():
    def __init__(self):
        self.tasks = []    
    
    def __taskDetails__(self):
        while 1:
            name = input("Uzduotis: ")
            if(self.__checkName__(name)):
                break
            print("Toks pavadinimas jau yra. Iveskite kita: ")
        imp = 0
        taskDate = datetime.now().date() - timedelta(days=1)
        #imp = int(input("Uzduoties svarba (1-5): "))
        while not self.__checkImportance__(imp):
            imp = int(input("Uzduoties svarba (1-5): ")) 
        while True:
            due = input("Uzduoties terminas (yy-mm-dd): ")
            due = list(map(int, due.split('-')))
            taskDate = dt(due[0], due[1], due[2])
            if self.__checkDate__(taskDate):
                break
            print("Negalimas terminas. Iveskite teisinga: ")
        
        return [name, imp, taskDate]

    def __checkImportance__(self, imp):
        if(1 <= imp <= 5):
            return True
        return False
    
    def __checkDate__(self, due):
        if(due > datetime.now().date()):
            return True
        return False
    
    def __checkName__(self, name):
        for task in self.tasks:
            if task.name == name:
                return False
        return True
         
    def addTask(self, *args):
        if len(args) == 0:
            print("Uzduoties duomenys")
            newTask = self.__taskDetails__()
            self.addTask(newTask[0], newTask[1], newTask[2])
        elif(len(args) == 3 and isinstance(args[0], str) and isinstance(args[1], int) and isinstance(args[2], dt)):
            print("Irasoma: ")
            print("     " + args[0] + ", " + str(args[1]) + ", " + str(args[2]))
            newTask = task(args[0], args[1], args[2])
            self.tasks.append(newTask)
            self.__sort__()
            self.__rewriteIndexes__()
    
    def tasksNumber(self):
        return len(self.tasks)
    
    def editTask(self, *args):
        if(len(args) == 0):
            print("Iveskite uzduoties indeksa: ")
            x = int(input())
            self.editTask(x)
        elif(len(args) == 1 and isinstance(args[0], int)):
            ind = args[0] - 1
            print("Pasirinkote redaguoti: {}".format(self.tasks[ind]))
            #pakeisti ta taska i temp
            ch = input("Nutraukti redagavima - 'q', ne - bet kuri kita simboli")
            if(ch == 'q'):
                return 0
            print("Atnaujinti duomenys:")
            editedTask = self.__taskDetails__()
            self.tasks[ind].name = editedTask[0]
            self.tasks[ind].importance = editedTask[1]
            self.tasks[ind].dueDate = editedTask[2]
            print("Atnaujinta uzduotis: {}".format(self.tasks[args[0]-1]))
            self.__sort__()
            self.__rewriteIndexes__()
    
    def __sort__(self):
        self.tasks.sort(key=lambda x: (x.dueDate, x.importance, x.name))    
    
    def showTasksNumber(self):
        print("Ilgis: " + str(len(self.tasks)) + "\n")
    
    def taskList(self):
        for task in self.tasks:
            print(task)
            
    def delTask(self, *args):
        if(len(args) == 0):
            print("Iveskite uzduoties indeksa: ")
            x = int(input())
            self.delTask(x)
        elif(len(args) == 1 and isinstance(args[0], int) and args[0] > 0):
            ind = args[0] - 1
            print("Panaikinama: " + self.tasks[ind].name)
            del self.tasks[ind]
            self.__rewriteIndexes__()
    
    def __rewriteIndexes__(self):
        for i in range(len(self.tasks)):
            self.tasks[i].ind = i+1
           
    def fromFile(self):       
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
        f.close()
        for item in tasks:
            self.toTask(item)
        self.__rewriteIndexes__()
            
    def toTask(self, item):
        ind = item.split('. ')
        elements = ind[1].split(', ')
        date = elements[2].split('-')
        date = list(map(int, date))
        due = dt(date[0], date[1], date[2])
        t = task(elements[0], int(elements[1]), due)
        self.tasks.append(t)
            
    def toFile(self):
        with open("tasks.txt", "w") as f:
            for item in self.tasks:
                f.write("{}. {}, {}, {}\n".format(item.ind, item.name, item.importance, str(item.dueDate)))
        f.close()