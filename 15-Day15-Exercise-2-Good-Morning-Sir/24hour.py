print("Greeting according to 24 hour clock format\n")
time=int(input("Enter the time in 24 hour format:"))
if time>=0 and time<=12:
    print("Good Morning")
elif time>=12 and time<=16:
    print("Good Afternoon")
elif time>=16 and time<=20:
    print("Good Evening")
elif time>=20 and time<=24:
    print("Good Night") 
else:
    print("Invalid Time")   