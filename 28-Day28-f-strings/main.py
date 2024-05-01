#FSTRINGS
#fstring is used to format strings in python
letter="hey my name is {} and i am from {}"
country ="Nepal"
name="Rijan"
print(letter.format(name,country))

letter="hey my name is {1} and i am from {0}"
country ="Nepal"
name="Rijan"
print(letter.format(name,country))

#using fstring
print(f"hey my name is {name} and i am from {country}")

txt="for only {price:.2f} dollars!"
print(txt.format(price=49.007))
age=39
print(f"hello , My name is {name} and i am {age}years old ")
