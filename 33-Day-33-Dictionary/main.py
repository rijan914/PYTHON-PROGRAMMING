#python dictionaries
#it is a collection of key value pairs 
#it is unordered
#it is mutable
#it is indexed
#it is represented by curly braces
#it is represented by key value pairs
#keys are unique
#keys are immutable
#values can be mutable or immutable     
#values can be duplicates
# dic={
#     "harry": "human being",
#     "spoon": "object"
# }
# print(dic["harry"])

from optparse import Values


roll ={
    7: "ronaldo",
    10: "messi",
    66: "rijan",
    11: "neymar",
    8: "toni kroos"
    #7 is key and ronaldo is value
}
print(roll)
print(roll.get('rmsi'))
print(roll[8])

#access multiple values

print(roll)
for key in roll.keys():
    print(roll[key])
    
for value in roll.values():
    print(value)
    print("yues")
