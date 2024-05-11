#ENUMERATE FUNCTION

marks = [90, 25, 67, 45,100, 80]

# index=0
# for mark in marks :
#     print(mark)
#     if (index ==4):
#         print("Harry, Awesome")
#     index +=1



for index, mark in enumerate(marks) :
    print(mark)
    if (index ==4):
        print("Harry, Awesome")
    
#so here we can see that enumerate function is used to get the index of the elements in the list.
#it is used to get the index and the value of the elements in the list.
# it is used to make the code more readable and understandable.

fruits =['apple', 'banana', 'mango', 'kiwi', 'grapes']
for index, fruit in enumerate(fruits):
    print(index,fruit)
    