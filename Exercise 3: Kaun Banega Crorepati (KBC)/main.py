#Create a program capable of displaying questions to user like KBC
#use list data type to store the questions and hteir correct answers.
#display the final amount the person is taking home after playing the game.
import os 
print("Welcome to Kaun Banega Crorepati (KBC)")
name=input("What is your name Sir/Madam?\n")
os.system('clear')
print("Hello",name,"Welcome to KBC")
print("lets proceed the game\n")

tuple=[1,2,3,4,5,6,7,8,9,10]
answers=[1,2,3,4,5,6,7,8,9,10]
uanswers=[1,2,3,4,5,6,7,8,9,10]

tuple[0]="what is the capital city of Nepal?"
tuple[1]="Mitochondria is power house of ?"
tuple[2]="What is the capital city of Canada?"
tuple[3]="What is the capital city of Japan?"
tuple[4]="founder of google is ?"
tuple[5]="What is the capital city of India?"
tuple[6]="What is the capital city of China?"
tuple[7]="What is the capital city of USA?"
tuple[8]="What is the capital city of UK?"
tuple[9]="What is the capital city of Australia?"

answers[0]="Kathmandu"
answers[1]="cell"
answers[2]="Ottawa"
answers[3]="Tokyo"
answers[4]="Larry Page"
answers[5]="New Delhi"
answers[6]="Beijing"
answers[7]="Washington D.C"
answers[8]="London"
answers[9]="Canberra"
right=0

options=[1,2,3,4,5,6,7,8,9,10]
options[0]="a.NEPAL","b.CANADA","c.Tokyo","d.Kathmandu"
options[1]="a.cell","b.mitochondria","c.ribosome","d.lysosome"
options[2]="a.Tokyo","b.Beijing","c.Ottawa","d.Washington D.C"
options[3]="a.Beijing","b.Tokyo","c.Washington D.C","d.London"
options[4]="a.Larry Page","b.Sergey Brin","c.Bill Gates","d.Mark Zuckerberg"
options[5]="a.New Delhi","b.Mumbai","c.Kolkata","d.Chennai"
options[6]="a.Beijing","b.Tokyo","c.Washington D.C","d.London"
options[7]="a.Beijing","b.Tokyo","c.Washington D.C","d.London"
options[8]="a.Beijing","b.Tokyo","c.Washington D.C","d.London"
options[9]="a.Beijing","b.Tokyo","c.Washington D.C","d.Canberra"

tick=[0,1,2,3,4,5,6,7,8,9]
tick[0]="d" or "D"
tick[1]="b" or "B"
tick[2]="c" or "C"
tick[3]="b" or "B"
tick[4]="a" or "A"
tick[5]="a" or "A"
tick[6]="a" or "A"
tick[7]="c" or "C"
tick[8]="d" or "D"
tick[9]="d" or "D"
i=0

for i in range(10):
    print("Here is the question no%i on your computer screen" % (i+1))
    print(tuple[i])
    print(options[i])
    uanswers[i]=input()
    if(uanswers[i]==answers[i] or uanswers[i]==tick[i]):
        os.system('clear')
        print("correct")
        right=right+1
    else:
        print("incorrect")
        break
    
if right == 0:
    print("congratulation")
    print("you won 0 rupees")
elif right == 1:
    print("congratulation")
    print("you won 1 housands rupees")
elif right == 2:
    print("congratulation")
    print("you won 10 thousands rupees")
elif right == 3:
    print("congratulation")
    print("you won 25 thousands rupees")
elif right == 4:
    print("congratulation")
    print("you won 50 thousands rupees")
elif right == 5:
    print("congratulation")
    print("you won 1 lakh rupees")
elif right == 6:
    print("congratulation")
    print("you won 2 lakh rupees")
elif right == 7:
    print("congratulation")
    print("you won 40000 rupees")
elif right == 8:
    print("congratulation")
    print("you won 25 lakh rupees")
elif right == 9:
    print("congratulation")
    print("you won 50 lakh rupees")
elif right == 10:
    print("Cheers to our Champion!!! ")
    print("congratulations")
    print("you won 1 karod rupees")
    

