#function arguments
def average(a,b):
    print("the average is ", (a+b)/2)
average(5,6)
#arguments types::

#default arguments
def average(a=2,b=3):
    print("the average is ", (a+b)/2)
average(5)

#keyword arguments
#order of arguments does not matter
def average(a,b):
    print("the average is ", (a+b)/2)
average(b=5,a=6)

#variable length arguments
#*a is used to pass multiple arguments  in a function   
#*a is a tuple
#*a is used to pass multiple arguments in a function

def average(*a):
    sum=0
    for i in a:
        sum+=i
    print("the average is ", sum/len(a))
average(5,6,7,8,9)

#required arguments
#required arguments are the arguments that are passed in a function
def average(a,b):
    print("the average is ", (a+b)/2)
average(5,6)