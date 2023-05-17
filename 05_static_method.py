class Sample:
    a = "uzair"
    b= "DevOps Engineer"

    @staticmethod #Apply static Method
    def greet():
        print(f"Good Morning , Mr {obj.a}")

obj = Sample()
# obj.a = "Ali" # Change the variable value
print(f"The Name is {obj.a} and the profession is {obj.b}")    
obj.greet()