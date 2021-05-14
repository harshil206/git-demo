# Write a programs to demonstrate the concept of assertions.

def checkingforVotingEligible(age):
    assert (age>18) ,"you are not eligible as your age is less than 18"
    return  age

print(checkingforVotingEligible(20))
print(checkingforVotingEligible(17))