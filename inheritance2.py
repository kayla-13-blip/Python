class Person:
         def __init__(self, fname, lname):
                 self.firstname = fname
                 self.lastname = lname
         def printname(self):
                 print(self.firstname, self.lastname)    
                   
class Student(Person):
        def __init__(self, fname, lname, year):
                self.graduationyear = year

                super().__init__( fname, lname)  
x = Student("Joey", "King", 2021) 
x.printname()  
print(x.graduationyear)                         
