"""
1. Creating Simple Classes
2. Difference between class and instance of that class
3. How to initialize  instance variable and class methods
"""

# Class Definition
class Employee:
    def __init__(self, first, last, pay, role):  # Here self is defined class instance(eg: emp_0, emp_1, emp_2), name, pay, role, email are instance variables, writing self.name = name is same as writing emp_0.name = "Rishabh", because during defn of class instance we pass this name info as Employee("rishabhmittal", 60000, "FSD")
        self.first = first
        self.last = last
        self.email = first+last + "@gmail.com"
        self.pay = pay
        self.role = role
    def fullName(self):
        return f"{self.first} {self.last}"

# Instances of Class
emp_0 = Employee("rishabh", "mittal", 600000, "FSD")
emp_1 = Employee("jivan","Fast", 100000, "Manager")
emp_2 = Employee("sushant","mittal", 1000000, "BA")

print(emp_0)
print(emp_1)
print(emp_2)



# Instance Variables(Contains Data specific to each instance) ---> THIS LINE IS MORE IMPORTANT TO UNDERSTAND

# emp_0.name = "Rishabh Mittal"
# emp_0.email = "rishabhmittal928@gmail.com"
# Employee 0 contains only name and email data

# emp_1.name = "Jivan"
emp_1.role = "Manager"
# Employee 1 contains only name and role data

# emp_2.name = "Sushant"
# emp_2.pay = 100000
# Employee 2 contains only name and pay data

print(emp_0.fullName())
print(emp_0.email)
print(emp_0.pay)
print(emp_1.role)


# Employee.fullName(emp_1) ## this calling the method on class itself, it requires to pass the self arg
# emp_1.fullName() ## this is calling the method on instance of class, it does not require to pass the self arg
# These does the same thing of printing the full name using fullName 'method'