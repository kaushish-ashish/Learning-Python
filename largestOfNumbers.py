#Check the Largest of 2 numbers
# a=int (input ("Enter 1st number"))
# b=int (input ("Enter 2nd number"))
# print("a is largest") if a>b else print("b is largest")

#Largest of 3 numbers
a=int (input ("Enter 1st number"))
b=int (input ("Enter 2nd number"))
c=int (input ("Enter 3rd number"))
if a>b and a>c:
    print("a is largest")
elif b>a and b>c:
    print("b is largest")
else:

    print("c is largest")
