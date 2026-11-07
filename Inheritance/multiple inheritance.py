class Person:
    def get_data(self,age,name):
        self.age=age 
        self.name=name 
    def show(self):
        print(f"Age:{self.age}")
        print(f"Name:{self.name}")

class Student:
    def get_data(self,per):
        self.per=per
    def show(self):
        print(f"Percentage:{self.per}")


class Emlpoyee(Person,Student):
    def get_data(self,age,name,per,sal):
        Person.get_data(self,age,name)
        Student.get_data(self,per)
        self.sal=sal
    def show(self):
        Person.show(self)
        Student.show(self)
        print(f"Salary:{self.sal}")

e1=Emlpoyee()
e1.get_data(23,"Girija",85.77,55000)
e1.show()          
