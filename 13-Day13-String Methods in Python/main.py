#strings are immutable
a="Rijan Santa Banta"
print(len(a))
print(a.upper())
print(a.lower())
#strings are immutable so new strings are created by operating on existing strings

#rstrip - removes white spaces from right side or removes trailing characters
#lstrip - removes white spaces from left side
#strip - removes white spaces from both sides
print(a.rstrip("n"))
print(a.lstrip("R"))
print(a.strip("ij"))

#replace
print(a.replace("Rijan","Elon Musk"))

#split()
#split changes string to list
print(a.split(" "))

#capitalize()
heading="introduction to python"
print(heading.capitalize())

#center()
print(len(heading))
print(heading.center(32))

#count()
print(heading.count("o"))

#endswith()
print(heading.endswith("n"))

#will i get ending with on between 2 to 8
print(a.endswith("on",2,20))

#find()
print(heading.find("an"))
#if found returns index else -1

#index()
#if not found then it raises error
print(heading.index("python"))

#isalnum()
#only returns true if only alphabets and numbers are present
print(heading.isalnum())
print(a.isalnum())

#isalpha()
print(a.isalpha())

#islower()
print(a.islower())
print(heading.islower())

#isprintable()
print(a.isprintable())
print(heading.isprintable())
#isprintable returns true if all characters are printable
#backslash is not printable

#isspace()
#returns true if all characters are white spaces
print(a.isspace())

#istitle
print(a.istitle())
print(heading.istitle())

#swapcase()
print(a.swapcase())

#title()
print(a.title())
print(heading.title())

