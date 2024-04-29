print("Greeting according to 12 hour clock format\n")
hour=int(input("enter the hour of current time\n"))
minute=int(input("enter the minute of current time\n"))
second=int(input("enter the second of current time\n"))
print("is it am or pm\n")
day=int(input("1 for am and 2 for pm\n"))
ftime=hour*60*60+minute*60+second
if(day==1):
    time=ftime
else:
    time=ftime+43200
if(time>0):
    if(time>0 and time<43200):
        print("good morning")
    elif(time>=43200 and time<64800):
        print("good afternoon")
    elif(time>=64800 and time<72000):
        print("good evening")
    else:
        print("good night")
else:
    print("Invalid Time")

    