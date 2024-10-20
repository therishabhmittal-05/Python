class Employee:
    num_emp = 0 # Class variable defined
    appraisal_percent = 1.05 # Class variable defined
    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last
        self.email = first+last + "@gmail.com"
        self.pay = pay
        Employee.num_emp += 1

    def fullName(self):
        return f"{self.first} {self.last}"
    
    def appraisal(self):
        self.pay = int(self.pay * self.appraisal_percent)

# Subclass and Inheritance
class Developer(Employee):
    appraisal_percent = 1.10 ## We changed the appraisal percent for developers only, without affecting appraisal percent for other Employee

    def __init__(self, first, last, pay, prog_lang, team):
        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang
        self.team = team
        
emp_0 = Employee("rishabh", "mittal", 600000)
emp_1 = Employee("jivan","Fast", 100000)
emp_2 = Employee("sushant","mittal", 100000)
dev_1 = Developer("ram", "goel", 90000, "python", "AI_team")
dev_2 = Developer("rohit","", 4000, "C++", "Dev_rel")
# print(dev_2.email)
# I have written pass in Developer class, but still getting the correct output, bcz Developer class inherits from Employee Class
# So we can access the attributes of Parent class here(Employee) 
# Python looks for init method in developer class, if not find it travel up the chain of inheritance(Mehtod resolution order)
# print(help(Developer))
# class Developer(Employee)
#  |  Developer(first, last, pay)
#  |
#  |  Method resolution order:
#  |      Developer
#  |      Employee
#  |      builtins.object
#  |
#  |  Methods inherited from Employee:
#  |
#  |  __init__(self, first, last, pay)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  appraisal(self)
#  |
#  |  fullName(self)
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors inherited from Employee:
#  |
#  |  __dict__
#  |      dictionary for instance variables
#  |
#  |  __weakref__
#  |      list of weak references to the object
#  |
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes inherited from Employee:
#  |
#  |  appraisal_percent = 1.05
#  |
#  |  num_emp = 2


# print(dev_1.pay)
# dev_1.appraisal()
# print(dev_1.pay)

# print(dev_2.prog_lang)
# print(dev_1.team)

# Manager Class
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print("-->" + emp.fullName())

mngr_1 = Manager("Ritvik", "Mittal", 120000, [dev_1, emp_0, emp_2 ] )
mngr_1.add_emp(dev_2) 
mngr_1.add_emp(emp_1) 
mngr_1.add_emp(dev_2) 
mngr_1.remove_emp(emp_2)
mngr_1.print_emp()
print(mngr_1.fullName())
print(mngr_1.email)

print(isinstance(dev_1, Manager))
print(isinstance(dev_1, Employee))
print(isinstance(mngr_1, Developer))

