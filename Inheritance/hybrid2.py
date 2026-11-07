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

class Desiganation:
    def get_data(self,post):
        self.post=post
    def show(self):
        print(f"Post:{self.post}")


class Employee(Student,Desiganation):
    def get_data(self,age,name,per,post,sal):
        Student.get_data(self,age,name,per)
        Desiganation.get_data(self,post)
        self.sal=sal
    def show(self):
        Student.show(self)
        Desiganation.show(self)
        print(f"Salary:{self.sal}")
e1=Employee()
e1.get_data(23,"Giru",87.99,"Devloper",560000)
e1.show()
