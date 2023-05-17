class test:
    a="uzair"
    b="MicroSoft"
    def takeData(self):
        print(f"The Name is {self.a} and the company is {self.b}")
obj=test()
obj.a="Ali"     # WE can change the variables by creating new instance variables
obj.b="YouTube"
obj.takeData()        