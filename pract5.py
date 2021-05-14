# Write a Python Program for OPERATOR OVERLOADING

class ExampleOperatorOverloading:
    def __init__(self,a):
        self.a=a
    
    def __add__(self,o):
        return self.a+o.a


        
op1=ExampleOperatorOverloading(5)
op2=ExampleOperatorOverloading(6)

print(op1+op2)