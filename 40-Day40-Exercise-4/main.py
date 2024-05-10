#secret code
#Write a python program to translate a message into secret code language .
#use the rules below to translate normal english into secret code language

#coding.
# if the word contains atleast 3 characters, remove the first letter and append it at the end 
# now append three random characters at the starting and the end of the word
# else:
#     simply reverse the string 

#eg: harry min+arry+hkid
#of fo
#decoding :
#if the word contains less than 3 characters, reverse it 
#else:
#remove 3 random characters from start and end. 
#now remove the last letter and append it to the beginning

#ask to user to whether you want to code or decode 
import random
import string
a=int(input("enter 1 for coding and 2 for decoding "))

def encodes():
    s=input("enter the string to encode ")
    l=s.split()
    for i in l:
        if(len(i)>=3):
            i=i[1:]+i[0]
            i=''.join(random.choices(string.ascii_lowercase,k=3))+i+''.join(random.choices(string.ascii_lowercase,k=3))
        else:
            i=i[::-1]
        print(i,end=' ')
        
def decode():
    s=input("enter the string to decode ")
    l=s.split()
    for i in l:
        if(len(i)<3):
            i=i[::-1]
        else:
            i=i[3:-3]+i[:1]
        print(i,end=' ')
        
if(a==1):
    encodes()
else:
    decode()
       