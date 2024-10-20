class Employee():
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + self.last + "@gmail.com"
    def fullName(self):
        return f"{self.first} {self.last}"
    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"
    def __str__(self) -> str:
        return f"{self.email} - {self.fullName()}"
emp_1 = Employee("Rishabh", "Mittal", "500000")
print(emp_1)
print(repr(emp_1))