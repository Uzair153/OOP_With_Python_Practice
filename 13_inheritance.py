class Person:
    Name="Uzair"
    Age="21"
    def display(self):
        print(f"The name is {self.Name} and his age is {self.Age}")

class Employee(Person):
    Name="ALI"

E=Employee()
E.display()