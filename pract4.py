# Write a Python Program for METHOD OVERRIDING

class Base1:
    def baseMethod(self):
        print("Method of base 1 class..")

class Base2:
    def baseMethod(self):
        print("Method of base 2 class....")

class Derived(Base1,Base2):
    def baseMethod(self):
        print("Method of derived class...")


obj=Derived()
print(obj.baseMethod())
print(Base1.baseMethod(obj))
print(Base2.baseMethod(obj))
    