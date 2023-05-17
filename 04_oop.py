class sample:
    def percentage(self):
        s=self.a + self.b + self.c 
        p= s/ self.tm * 100
        print(f"The percentage is {p}")
    def takeValeu(self):
        self.a=int(input("The Marks of Math : "))
        self.b=int(input("The Marks of phy : "))
        self.c=int(input("The Marks of computer : "))
obj1=sample()
obj2=sample()
obj1.tm=300
obj2.tm=300
obj1.takeValeu()
obj2.takeValeu()
obj1.percentage()
obj2.percentage()