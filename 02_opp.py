class Number:
    def takeValue(self):
        self.a=int(input("Enter the  1st Number : "))
        self.b=int(input("Enter the  2nd Number : "))
    def sumValue(self):
        c=self.a + self.b
        print(f"The sum is {c}")
obj=Number()
obj.takeValue()
obj.sumValue()        
    