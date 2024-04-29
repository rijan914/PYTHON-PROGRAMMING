print("Welcome to Tarkari Pasal")
goji_ma_dam=int(input("how much money do you have?"))
apple_price=100
orange_price=50
banana_price=40
if(goji_ma_dam>=apple_price):
    print("You can buy apples or oranges or bananas")
elif(goji_ma_dam>=orange_price):
    print("You can buy oranges or bananas")
elif(goji_ma_dam>=banana_price):
    print("You can buy bananas only")
else:
    print("you cannot buy anything")
    