class Person:
    def get_data(self,age,name):
        self.age=age 
        self.name=name 
    def show(self):
        print(f"Age:{self.age}")
        print(f"Name:{self.name}")

class Student(Person):
    def get_data(self,age,name,per):
        super().get_data(age,name)
        self.per=per
    def show(self):
        super().show()
        print(f"Percentage:{self.per}")

class Employee(Person):
    def get_data(self,age,name,sal):
        super().get_data(age,name)
        self.sal=sal
    def show(self):
        super().show()
        print(f"Salary:{self.sal}")

s1=Student()
s1.get_data(20,"Arjun",88.55)
s1.show()

e1=Employee()
e1.get_data(23,"ganesh",88000)
e1.show()