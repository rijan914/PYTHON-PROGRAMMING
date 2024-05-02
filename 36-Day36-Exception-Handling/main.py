#exception handling
a=input("enter the number:")
print("multiplication table of {a} is :")
try:
    for i in range(1,11):
     print(f"{a} * {i} = {int(a)*int(i)}")
except Exception as e:
    print("sorry something went wrong")
    print("invalid input")
    
print("some lines of code")
print("end of program")

