mylist = ["Luffy", "Sasuke","Sakura","Nami"]
def sum(a,b):
    return a+b

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print("Hello, " + self.fname + " " + self.lname)
    