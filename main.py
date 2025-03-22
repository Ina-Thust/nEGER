#class Student:
#    amount_of_students = 0
#    def __init__(sel, height = 160):
#        sel.height = height
#        Student.amount_of_students += 1
#
#print(Student.amount_of_students)
#NICK = Student()
#kate = Student(height=165)
#print(NICK.amount_of_students)
#print(Student.amount_of_students)

#class Student:
#    height = 160
#    def __init__(self):
#        print(self.height)
#        Student.height += 10
#        print(self.height)
#nick = Student()
#kate = Student()
#nick = Student()
#kate = Student()

#class Student:
#    def __init__(self):
#        self.height = 170
#    height = 160
#    def printir(self):
#        print(self.height)
#    def change_height(self, new_height):
#        self.height = new_height
#nick = Student()
#nick.printir()
#nick.change_height(174)
#nick.printir()

class Student:
    def __init__(self, n = None, h = 290):
        self.n = n
        self.h = h
    def __bool__(self):
        return self.n != None
    def __len__(self):
        return self.h
    def __del__(self):
        print("Студент все...")
nick = Student()
print(nick.__bool__())
print(nick.__len__())
print(len(nick))
print(bool(nick))
