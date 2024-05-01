#operations on tuple
#changing tuple to list and again list to tuple to append the data items

countries=("nepal","india","china","usa","uk")
temp=list(countries)
temp.append("GHANA")
temp.pop(2)
temp[2]="Mount Everest"
countries=tuple(temp)
print(countries)

tup2=countries[1:3]
print(tup2)

tuple1=(13,2,32,2,3,3,4,5,6,73,3,3,2,8,9)
res=tuple1.count(3)
res1=tuple1.index(3,0,9)
#it shows the index of 3 in tuple1 from 0 to 9
print(res1)
res=tuple1.index(4)

#no of occurences of 3 in tuple1
print("count of 3 in tupe1 is :",res)