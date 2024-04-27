#calculator
'''
author : Rijan
course : Code with Harry
'''
print("WELCOME TO RIJAN CALCULATOR")
a=input("enter the number \n")
b=input("enter another number\n")
inp=input("enter the operation you want to perform\n")
if inp=="+":
    print("sum of a and b is ",int(a)+int(b))
elif inp=="-":
    print("difference of a and b is ",int(a)-int(b))
elif inp=="*":
    print("product of a and b is ",int(a)*int(b))
elif inp=="/":
    print("division of a and b is ",int(a)/int(b))
elif inp=="%":
    print("remainder of a and b is ",int(a)%int(b))
elif inp=="**":
    print("a to the power of b is ",int(a)**int(b))
elif inp=="//":
    print("quotient of a and b is ",int(a)//int(b))
else:
    print("invalid input")
