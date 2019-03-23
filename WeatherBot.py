# Talk to me about the weather today!
# Link: https://py3.codeskulptor.org/#user303_86WogR5aok_0.py

import random

print("Hi there! What's your name?")

name = input("My name is...")

print("Nice to meet you " + name + ". I'm WeatherBot!")

life = input("How's life? Good? ")

if(life == "Yes" or life == "yes" or life == "yeet" or life == "Yeet"):
    print("\nI'm glad to hear that! My life's been pretty good as well.")
else:
    print("\nI'm sorry, I wish I could help.")
    do = input("Would a boop make you feel better? ")
    if(do == "Yes" or do == "yes" or do == "yeet" or do == "Yeet"):
        print("\nBoop!")
    else:
        print("\nAw okay. Boops are pretty great though.\n")

weather = input("So tell me, " + name + ", is it cold outside today? ")

if(weather == "Yes" or weather == "yes" or weather == "yeet" or weather == "Yeet"):
    print("\nBrr. What temperature in Farenheit is it? ")
    temperature = input("Hm?")
    if(temperature == "idk" or temperature == "IDK" or temperature == "I don't know"):
        print("\nIt's okay if you don't know. Farenheit is funky that way.")
    elif(int(temperature) >= 75):
        print("\nWait a second, that's not cold! ")
        secondweather = input("Are you sure it's cold?? ")
        if(secondweather == "Yes" or secondweather == "yes" or secondweather == "yeet" or secondweather == "Yeet"):
            secondweatheryes = random.choice(["Oooookay then, if you're sure...", "You should probably go put on a jacket then if you think it's cold.", "You might want to check again...?"])
            print("\n" + secondweatheryes)
        else:
            print("\nI'm confused now, but okay, if you say so!")
    elif(int(temperature) <= 75 and int(temperature) >= 30):
        print("\nWow, that is really cold!")
        jacket = input("Are you wearing a jacket?")
        if(jacket == "yes" or jacket == "Yes" or jacket == "yeet" or jacket == "Yeet"):
            print("Oof, maybe go put on another one? And several blankets?")
        else:
            print("Maybe you should go put one on then...")
    elif(int(temperature) <= 30):
        freezingtemp = random.choice(["Oh my gosh, that's so cold!! Don't get hypothermia!", "Woah, you better stay inside and keep warm!", "Oh jeez, that sounds bad. Drink hot chocolate!"])
        print(freezingtemp)
    
else:
    print("\nSo then is it warm outside? ")
    notcold = input("Hm?")
    if(notcold == "Yes" or notcold == "yes" or notcold == "yeet" or notcold == "Yeet"):
        print("Warm is a wonderful temperature! ")
        warmact = input("Are you going to do anything fun or exciting later? ")
        if(warmact == "Yes" or warmact == "yes" or warmact == "yeet" or warmact == "Yeet"):
            warmactyes = random.choice(["Well, I hope you have fun!", "Lucky! Have a great time!", "That's awesome to hear!"])
            print(warmactyes)
        else:
            print("Aww, I'm sorry. I'm not doing anything fun or exciting either, so I know how you feel!")
    else:
        print("\nSo then I'm assuming it's hot outside. ")
        notcoldwarm = input("Is it? ")
        if(notcoldwarm == "Yes" or notcoldwarm == "yes" or notcoldwarm == "yeet" or notcoldwarm == "Yeet"):
            print("\nHow hot? ")
            hottemp = int(input("In Farenheit? "))
            if(hottemp >= 75):
                hottempans = random.choice(["Ah, nice! I love hot days!", "Hot days are perfect for beach days! Why not hang out there?", "Better turn up the AC!", "Put on sunblock if it's also sunny!"])
            elif(hottemp <= 75 and hottemp >= 30):
                print("Hey, wait a second! That's not that hot! ")
                hotcheck = input("Are you sure it's hot out?")
                if(hotcheck == "Yes" or hotcheck == "yes" or hotcheck == "yeet" or hotcheck == "Yeet"):
                    print("Okay, if you're sure...")
                else:
                    print("I knew it! You're just trying to trick me! ;)")
            elif(hottemp <= 30):
                print("WOAH, that's not hot at all! How are you not freezing yet??")
        else:
            print("\nYou're beginning to confuse me...so then what is the weather outside? ")
            confuseweather = input("What's the weather if it's not cold, warm, or hot? ")
            print("Ah, that makes sense now. I gotchu! \n\nThanks for talking to me! \nEven if your answers were a little confusing :p")

print("\nI hope you have a nice day!")
            
