
#sets
#sets are unordered collections of unique elements
#sets are defined by values separated by commas inside curly braces
#sets are mutable, but elements in sets must be immutable   
#sets do not have duplicates
#sets are unordered, so we cannot access elements by index

s={1,2,3,4,5,6,7,8,9,10}
print(s)
print(type(s))
p=s
print(p)

#try to create an empty set.check using the type() function whether the type of your variable is a set 
z={ }
print(type(z))
#it is not a empty set but a dictionary 
#so to make a empty set we wrtie
z=set()
print(type(z))
