class Person:
    def __init__(self,fname,lname,age):
        self.firstname = fname
        self.lastname = lname
        self.age = age
    
    def printName(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self,fname,lname,age):
        Person.__init__(self,fname,lname,age)
    pass

x = Person("John","Doe",34)
x.printName()

y = Student("Mike","Olsen",55)
y.printName()
