class sample:
    def __init__():
        {}
    def __init__(self, name , Class , RollNo): #Here Constructor is called 
        self.name=name
        self.Class=Class
        self.RollNo=RollNo
    def display(self):
        print(f"The Name is : {self.name}")
        print(f"The Class is : {self.Class}")
        print(f"The RollNo is : {self.RollNo}")
a=sample("uzair","BSIT","bsf32342")
a.display()