
class A:
    Name="Uzair"
    def method_a(self):
        print("Method A from class A")


class B:
    position="DevOps Engineer"
    def method_b(self):
        print("Method B from class B")


class C:
    location="Canada"
    def method_c(self):
        print("Method C from class C")


class D(A, B, C):
    def __init__(self):
        print(f"The employee is {self.Name} , his role is as a {self.position} and he is from {self.location}")
    def method_d(self):
        print("Method D from class D")


d = D()


d.method_a()  
d.method_b()  
d.method_c()  
d.method_d()  