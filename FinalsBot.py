#Talk to me about finals and school!
#CodeSkulptor3 Link: https://py3.codeskulptor.org/#user303_BEUZ17B1Tb_1.py

#MODULES

import random
import time

###########
#VARIABLES (order of first appearance)
#Intro / Doing Well in School Variables
nameadj = random.choice(["an amazing", "a wonderful", "an awesome", "a pretty", "a cool", "a beautiful"])
adj = random.choice(["amazing", "wonderful", "intelligent", "awesome", "determined", "cool", "courageous"])
schooladj = random.choice(["amazing", "wonderful", "intelligent", "super smart", "awesome", "determined", "cool", "courageous"])

#Finals Variables
encourage = random.choice(["Ahh, good luck!", "You'll do amazing!", "I believe in you!", "Finals are easy for an amazing person like you!", "It'll all be over soon.", "Finals are a drag, but you got this!"])
sympathy = random.choice(["Aww, I'm sorry to hear that.", "Oof, that sucks...", "That's harsh.", "Ah, I know how you feel."])
bestofluck = random.choice(["\nBest of luck to you mate.", "\nBest of luck!", "\nHope you do well!", "\nGood luck!", " ", " "])
lucky = random.choice(["Wow, lucky!", "You don't have to worry at all then!", "Haha, nice!", "Wish I was you :p"])

#Guessing Num Months Variables
finalswarning = random.choice(["Though, it's better to get started studying earlier than later.", "Start studying now so you don't have a pileup of work later!", "You've got some time to chill then!", "Don't let your guard down though!", "Finals come up fast, so be careful."])

#Outro Variables
talkingtouseradj = random.choice(["super fun", "amazing", "great", "wonderful", "awesome", "fun", "enlightening"])

#############

#INTRO

print("Hi! I'm your friendly next door neighbor, Chat Bot! What's your name?")


#ASK NAME

name = input("What's your name?")
name = name.capitalize()

print("\n--- " + name + "\n")

print(name + "? Wow, that's such " + nameadj + " name! It's very nice to meet you " + name + "!")

#DOING WELL IN SCHOOL

print("\nAre you doing well in school?")
school = input("Yes? No?")

print("\n--- " + school + "\n")

if(school == "Yes" or school == "yes"):
    print("That's great to hear! I knew you could do it 'cuz you're " + adj + "!")
elif(school != "Yes" or school != "yes"):
    print(sympathy + " \nBut don't worry! \nYou're " + schooladj + ", so I know you'll be saying yes in no time!")

#FINALS

print("\nDo you have finals coming up?")
finals = input("Yes? No?")
print("\n--- " + finals + "\n")
if(finals == "Yes" or finals == "yes"):
    print(encourage)
elif(finals != "Yes" or finals != "yes"):
    print(lucky)
    
#GUESS # OF MONTHS UNTIL FINALS
    
print("\nCan I try to guess how many months it is until your finals?")
guess = input("Yes? No?")
print("\n--- " + guess + "\n")
if(guess == "Yes" or guess == "yes"):
    nummonths = random.randint(1, 12)
    print("Alright let's see...is it..." + str(nummonths) + " months until your finals? Yes or no?")
    monthconfirm = input("Yes? No?")
    print("\n--- " + monthconfirm + "\n")
    if(monthconfirm == "Yes" or monthconfirm == "yes"):
        print("Wow, I actually got it! Wasn't expecting that hahaha.")
        if(nummonths >= 4):
            print("So you have some time before finals! \n" + finalswarning)
        elif(nummonths <= 3):
            print("Ooh, those are kind of close! Be careful; you can never be overprepared.")
    if(monthconfirm == "No" or monthconfirm == "no"):
        print("Aw, man. Well, you can't guess them all.")
        print("\nSo then how many months do you actually have until your finals? ")
        actualmonth = int(input("Hm?"))
        print("\n--- " + str(actualmonth) + "\n")
        if(actualmonth >= 4):
            print(str(actualmonth) + " months?? You've got plenty of time! \nThough you should start studying earlier rather than later.")
        elif(actualmonth <= 3 and actualmonth > 1):
            print(str(actualmonth) + " months isn't that long. Better start studying now!")
        elif(actualmonth == 1):
            print("AHHH, 1 month?? That's not a long time until finals at all! " + bestofluck)
        elif(actualmonth == 0):
            print("Oh jeez, that means you have them this month." + bestofluck)

else:
    print("Aww, okay. T^T I'm sad now.")
    print("Just kidding! It's okay, I forgive you.")
    
    
#GOODBYE

if(finals == "Yes" or finals == "yes"):
    bonusshulk = random.randint(1, 10)
    if(bonusshulk == 8):
        print("\nThis is the " + name + "'s power! Acing finals!")
    elif(bonusshulk != 8):
        print(" ")
    print("\nIt was " + talkingtouseradj + " to talk to you! \nHope to see you again later! \nTell me how your final goes later :)")
else:
    print("\nIt was " + talkingtouseradj + " to talk to you! \nHope to see you again later!")
