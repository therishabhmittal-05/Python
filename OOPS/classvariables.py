"""
1. Difference Between Class Variable and Instance Variable
2. Use of Class Variable-> a. Using Instance of Class b. Using Class name
3. Updating Class Variable for instance of class and whole class
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
        # self.pay = int(self.pay * Employee.appraisal_percent) ## using class variable by class name (Good, actually logically)
        self.pay = int(self.pay * self.appraisal_percent) ## using class variable by instance of the class (little confusing, but still good), Also this is more useful lets us control if we want to change the appraisal amt or not for an instance of class

    # first, last, pay, role are instance variables (unique to each instance of class)
    # class variables are same for each instance of the class

# Instances of Class
emp_0 = Employee("rishabh", "mittal", 600000, "FSD")
emp_1 = Employee("jivan","Fast", 100000, "Manager")
emp_2 = Employee("sushant","mittal", 1000000, "BA")

# print(emp_1.pay)
# emp_1.appraisal()
# print(emp_1.pay)

print(emp_0.__dict__)
#  {'first': 'rishabh', 'last': 'mittal', 'email': 'rishabhmittal@gmail.com', 'pay': 600000, 'role': 'FSD'}

emp_0.appraisal_percent = 1.10 ## Change in appraisl percent of emp_0 'ONLY'

print(emp_0.__dict__)
# {'first': 'rishabh', 'last': 'mittal', 'email': 'rishabhmittal@gmail.com', 'pay': 600000, 'role': 'FSD', 'appraisal_percent': 1.1}

print(emp_0.appraisal_percent)
print(Employee.appraisal_percent)

Employee.appraisal_percent = 1.10 ## Change in appraisl percent of 'WHOLE' class
print(emp_0.appraisal_percent)
print(Employee.appraisal_percent)


# print(Employee.__dict__)
print(Employee.num_emp)
