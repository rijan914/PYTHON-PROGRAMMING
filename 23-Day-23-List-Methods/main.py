#list methods
l=[2,3,4,5,6,7,8,9]
l.append(7)
print(l)

names=['rijan','neymar','messi','ronaldo']
# names.append('Toni Kroos')
# print(names)
names.sort(reverse=True)
print(names)

print(l.index(5))

print(l.count(3))
l.append(88)
m=l.copy()
m[0]=0
print(m)
print(l)

#insert()
l.insert(0,33)
print(l)

#extend()
m=[99,88,77,66]
l.extend(m)
#extends l with m
print(l)

k=l+m
print(k)
#concatenates l and m
