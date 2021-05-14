# Write a Python Program for MULTIPLE INHERITANCE

class Person:
    def __init__(self,name):
        self.name=name
    
    def getName(self):
        return self.name

class Address:
    def __init__(self,address):
        self.address=address
    
    def getAddress(self):
        return self.address


class Employee(Person,Address):
    def __init__(self,name,salary,address):
        self.salary=salary
        Person.__init__(self,name)
        Address.__init__(self,address)

    def getsalary(self):
        return self.salary
    



Emp=Employee("harshil","18000","Ahmedabad")
print(Emp.getName())
print(Emp.getsalary())
print(Emp.getAddress())