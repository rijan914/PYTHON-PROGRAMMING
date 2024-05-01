#tuple
tup=(2,3,4,5,6,342,7,8,9,"rijan","neymar","messi","ronaldo")
print(type(tup))
#tuple is an ordered collection of elements enclosed in ()
#tuple is immutable
print(tup[0])
print(tup[-1])
#tuple can have multiple data types
#tuple can have duplicate values


if 342  in tup:
    print("yes 342 is presetnt in tuple")
    
tup2=tup[1:4]
print(tup2)
print(len(tup))