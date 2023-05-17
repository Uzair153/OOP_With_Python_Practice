class Number:
    def __init__(self, num):
        self.num = num
        
    def __add__(self, other):
        print("Let's Add")
        return self.num + other.num
        
n1 = Number(4)
n2 = Number(6)
result = n1 + n2
print(result)
