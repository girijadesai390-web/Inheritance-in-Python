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

s1=Student()
s1.get_data(21,"Alex",85.33) 
s1.show()                      

s2=Student()
s2.get_data(23,"Girija",83.40)
s2.show()