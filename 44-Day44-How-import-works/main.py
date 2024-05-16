#importing in python
#importing in python is the process of loading code from a python  module into the current scrpit 
#this allows you to use the fucntions and variables defined in the module in your current script as well as any additional modules that the imported module may depend on 

# eg import math
# import math 
# #once a module is imporrted we can use any of the functions and variables defined in the module by using the dot notation. 
# result = math.sqrt(9)
# print(result)

# from math import sqrt , pi
# result= sqrt(9)*pi
# print(result )

# from math import *
# result= sqrt(9)*pi
# print(result )

from math import pi,sqrt as s
result= s(9)*pi
print(result )

# import math as m 
# result=m.sqrt(9)*m.pi
# print(result)

# import math 
# print("functions of math module:")
# print(dir(math))

# print(math.nan,type(math.nan))

# from rijan import welcome,rijan
# print(welcome())
# print(rijan)

# from rijan import *
# print(welcome())
# print(rijan)
import rijan as rizz
rizz.welcome()
