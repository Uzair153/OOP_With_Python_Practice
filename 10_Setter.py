class Employee:
    Company = "FaceBook"
    base_salary = 55000
    bonus = 5000

    @property
    def total_salary(self):
        return self.base_salary + self.bonus

    @total_salary.setter
    def total_salary(self, value):
        self.bonus = value - self.base_salary

e = Employee()
print(e.total_salary)
e.total_salary = 65000
print(e.total_salary)
print(e.bonus)
