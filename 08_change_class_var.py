class Employee:
    company= "Google"
    selary = 60000

    def display(self):
        print(f"The Company Name is {self.company} and his selary is {self.selary}")

    def changeValue(self , sal): # Here the valeu of class object is change
        self.__class__.selary=sal
            

uzair=Employee()
uzair.display()
# uzair.selary=70000
uzair.display() # its display the latest value , that we change for selary as a instance object
print(Employee.selary)
uzair.changeValue(80000)
print(Employee.selary) # its display the latest value , that we change for selary as a class object
uzair.display()