#rolling of a dice game
# number guessing game
print("Welcome to number guessing game in dice")
name=("enter your name: ")
import random
f="y"
a=0
while f=="y":
    com=random.randint(1,6)
    user=int(input("enter your no. in between 1 to 6 please: "))
    if user==com:
        a=a+1
        print("you chose",user,"and computer chose",com)
        print("congratulation you win")
    else:
        print("you chose",user,"and computer chose",com)
        print("you lost sorry")
    f=input("do you want to play more y/n: ")
print(name,"scored:",a)
print("thank you for playing game")
