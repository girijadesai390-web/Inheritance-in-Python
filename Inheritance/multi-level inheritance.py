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

class Employee(Student):
    def get_data(self, age, name, per,sal):
        super().get_data(age, name, per)
        self.sal=sal 
    def show(self):
        super().show()
        print(f"Salary:{self.sal}")

e1=Employee() 
e1.get_data(22,"girija",85.66,30000)
e1.show()