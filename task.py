from datetime import date 
class task:
    def __init__(self, name, importance, dueDate):
        self.ind = -1
        self.name = name
        self.importance = importance
        self.dueDate = dueDate
    def __str__(self):
        return "{}. {:<25} {:<3} {:<12}".format(self.ind, self.name, str(self.importance), str(self.dueDate))