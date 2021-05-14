# Write  a  programs  to  demonstrate  the  concept  of  exception handling.

a=int(input("enter divisor : "))
b=int(input("enter divider : "))

try:
    c=a/b
    print(c)

except ArithmeticError:
    print("Exception........You have divide number by 0....")