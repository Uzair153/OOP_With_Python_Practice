class A:
    company="Facebook"
    Name="Uzair"
    def __init__(self):
        print("This is Base class")
class B(A):
    def __init__(self):
        print("This is child class")
        print(f"The name is {self.Name} and the company is {self.company}")
    
a=A()
b=B()
