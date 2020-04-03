class dueDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __str__(self):
        return str(self.year) + "-" + str(self.month) + "-" + str(self.day) 