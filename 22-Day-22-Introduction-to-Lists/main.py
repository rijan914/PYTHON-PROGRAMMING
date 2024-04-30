#list 
l=[2,3,4,5,6,7,8,9]
print(l)
print(type(l))
print(l[0])
print(l[1]) 
#list are mutable , ordered collection of data items 
#list can have multiple data types
#list can have duplicate values
#list can have nested list
#tuple are not changeable but list are changeable
lsis=[2,3,4,5,6,7,8,9,'rijan','shrestha',True]
print(lsis)
print(type(lsis))
print(lsis[0])

#list indexing
#positive indexing
colors=['red','green','blue','yellow']
print(colors[0])

#negetive indexing
print(colors[-1])
#converting negetive indexing into positive indexing 
print(len(colors)-1)
print(colors[3])

#checking is 7 in the list calles lsis
if 7 in lsis:
    print("yes")
else:
    print("no")

if "green" in colors:
    print("yes")
else:
    print("no")

print(colors[0:-1])
print(colors[0:3])
print(len(colors))
print(colors[0:4:2])

#list comprehension
#list comprehension is a way to create list in python
#it is a short way to create list
lst=[i*i for i in range(4) if i%2==0]
print(lst)

doc_name=['rijan','neymar','messi','ronaldo']
nameswith0=[item for item in doc_name if(len(item)>5)]
print(nameswith0)

players=["ronaldo","messi","neymar","mbappe","modric","sunil"]
goats=[item for item in players if item=="ronaldo" or item=="messi"]
print(goats)