import time 
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
print(t)

if(hour>0 and hour<12):
    print("Good Morning")
elif(hour>=12 and hour<16):
    print("Good Afternoon")
elif(hour>=16 and hour<20):
    print("Good Evening")
elif(hour>=20 and hour<24):
    print("Good Night")
# j=0
# while True:
#     j=j+1
#     print(t)

