#matchcase 
x=int(input("enter the number"))
match x:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case 5:
        print("five")
    case 6:
        print("six")
    case 7:
        print("seven")
    case 8:
        print("eight")
    case 9:
        print("nine")
    case 10:
        print("ten")
    case _:
        print("Invalid number")