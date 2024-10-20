"""
1. Regular Methods
2. Class Methods
3. Static Methods
"""
class Employee:
    num_emp = 0 # Class variable defined
    appraisal_percent = 1.05 # Class variable defined
    def __init__(self, first, last, pay, role): 
        self.first = first
        self.last = last
        self.email = first+last + "@gmail.com"
        self.pay = pay
        self.role = role
        Employee.num_emp += 1

    def fullName(self):
        return f"{self.first} {self.last}"
    
    def appraisal(self):
        self.pay = int(self.pay * self.appraisal_percent)

    @classmethod
    def set_appraisal_amt(cls, amount):
        cls.appraisal_percent = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay, role = emp_str.split('-')
        return cls(first, last, pay, role)
    @staticmethod
    def is_working(_date):
        if _date.weekday() == 5 or _date.weekday() == 6:
            return False
        return True
        

emp_0 = Employee("rishabh", "mittal", 600000, "FSD")
emp_1 = Employee("jivan","Fast", 100000, "Manager")
emp_2 = Employee("sushant","mittal", 1000000, "BA")

pay = emp_0.pay
print(emp_0.appraisal_percent)
emp_0.appraisal()
print(emp_0.pay)

emp_0.pay = pay
Employee.set_appraisal_amt(1.10) ## Using class Mehtod, runing class method by class itself (Which is only Good !!)
# Employee.appraisal_percent = 1.10 ## Doing this is same as what set_appraisal_amt is doing
emp_0.appraisal()

print(emp_0.appraisal_percent)
print(emp_0.pay)

# Class Methods as Alternative Constructors (as eg: __init__)

# Use case: Somebody using our Employee class aggressively, but is getting the input in form of single str of required instance variables each time we have to parse that string and then create class instance for it
# Instead we can create a custom constructor "from_string" which parse and return the new class instance


emp_3_str = "raghav-goyal-30000-clerk"

emp_3 = Employee.from_string(emp_3_str)

print(emp_3.email)

# Static Method: when you are not usign instance or class anywhere in the method
# They are included bcz they have some logical connection with Class

import datetime
_date = datetime.date(2024, 10, 20)
print(Employee.is_working(_date))
