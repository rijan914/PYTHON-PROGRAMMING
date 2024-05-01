# #recursion
# # mul=1
# # n=int(input("enter a number"))
# # for n in range(1,n+1):
# #     mul=mul*n

# # print(mul)


# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
        
# print(factorial(3))
# print(factorial(4))
# print(5*factorial(3))
               
        
# #fibonacci 
# #   f0=0
# #     f1=1
# #     f2=f1+f0
# #     f3=f1+f2
# #     f4=f3+f2
# #     fn=f(n-1)+f(n-2)
# a=0
# b=1
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fib(n-1) + fib(n-2)

n = int(input("Enter a number: "))
print(fib(n))