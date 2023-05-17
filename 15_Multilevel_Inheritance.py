class A :
    company="RedHat"
    job_position="DevOps Engineer"
    location = "USA"
    def __init__(self, name):
         self.name=name
    def display_location(self):         
        if self.location == "canada":
            print(f"{self.name} is from Canada")
        else:
            print(f"{self.name} is from UK")
class B(A) :
    location="canada"
    def display(self):
         print((f"The Job Position is {self.job_position}"))
class C(B):
     location="UK"

b = B
b=B("Uzair")
b.display_location()
b.display()

# c = C
# c=C("Uzair")
# c.display_location()
# c.display()

