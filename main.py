import time
timestamp = time.strftime('%H:%M:%S')
htimestamp = int(time.strftime('%H'))
mtimestamp = int(time.strftime('%M'))
stimestamp = int(time.strftime('%S'))
if htimestamp>=0 and htimestamp<=12:
    print("Good Morning")
elif htimestamp>=12 and htimestamp<=16:
    print("Good Afternoon")
elif htimestamp>=16 and htimestamp<=20:
    print("Good Evening")
elif htimestamp>=20 and htimestamp<=24:
    print("Good Night")
else:
    print("Invalid Time")
print("The time is",timestamp)
