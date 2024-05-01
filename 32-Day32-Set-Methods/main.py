#set methods
s1={1,2,3,4,5,6}
s2={3,5,8,7,"ram","shyam"}
# #union
# print(s1.union(s2))
# print(s1,s2)
# s1.update(s2)
# print(s1)

# intersection
# print(s1.intersection(s2))
# s1.intersection_update(s2)
# print(s1)

#symmetric difference
print(s1.symmetric_difference(s2))

#isdisjoint()
#it means that two sets do not have any common element
cities1={"delhi","mumbai","chennai","kolkata"}
cities2={"pune","sadf","nashik","aurangabad"}
print(cities1.isdisjoint(cities2))

#issuperset()
#it returns true if a set has every element of another set
cities3={"delhi","mumbai","chennai","kolkata"}
print(cities1.issuperset(cities3))

#issubset()
#it returns true if every element of a set is present in another set
print(cities3.issubset(cities1))
#difference between issubset and issuperset is that issubset returns true if every element of a set is present in another set
#while issuperset returns true if a set has every element of another set
cities3.add("kalinchowk")
print(cities3)
cities3.remove("kalinchowk")
print(cities3)
cities3.discard("kalinchowk")
print(cities3)

#pop()
#it removes a random element from the set
cities3.pop()
#del
#it removes the set completely
del cities3

#clear()
#it removes all the elements from the set
info={"name","age","address","phone"}
info.clear()
print(info)