#dicitonary methods
ep1={122:32,123:34,124:35,125:36,126:37}
ep2={127:38,128:39,129:40,130:41,131:42}
# ep1.update(ep2)
# print(ep1)
#set are unordered , dictonary are ordered
# ep1.clear
# print(ep1)

empt={ }
print(empt)
ep1.popitem()
#removes the last item from the dictonary 
ep1.pop(122)
print(ep1)
#diference in set and dictonary are that set is defined by values separated by commas inside curly braces
#while dictonary is defined by key value pairs

# del ep1
# print(ep1)
del ep1[123]
print(ep1)