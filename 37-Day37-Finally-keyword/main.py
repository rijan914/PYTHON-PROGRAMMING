print("finally - clause")
#used to execute some code after the try block, and before the code block
# whether the exception is raised or not.
#The finally clause in Python is used for specifying cleanup actions that must be executed under all circumstances.
def fun1():
    try:
        l=[1,2,3,4,5]
        i=int(input("enter the index:"))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("i am always executed")
    #here function returns but also the finally block is executed    
x=fun1()
print(x)
