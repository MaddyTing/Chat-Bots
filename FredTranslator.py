# Translates Fred's words

print("Hello there! What's your name?")

name = input("My name is...")
name = name.capitalize()

print("\n--- " + name)
print("\nNice to meet you " + name + ". I'm the one and only FredTranslator.")

print("\nYou must be here for some reason. What happened? FredTalk?")

fredtalk = input("O.o")
fredtalk = fredtalk.capitalize()

if(fredtalk.find("Y") > -1 or fredtalk.find("y") > -1):
    print("\n--- " + fredtalk)
    print("\nSo you just got a FredTalk. Aw man, I'm sorry to hear that :(")
    print("\nWhat did he say to you?")
    
    # Listing Options
    print("1: \"You need to go faster\"")
    print("\n2: The 'I'm not mad, I'm just disappointed' face")
    
    # Select option
    fredsaid = int(input("O.o"))
    
    # Interprets Option
    if(fredsaid == 1):
        optiona = "sadf"
        print("\n--- Fred: \"" + optiona + "\"")


else:
    print("\nIf you didn't get a FredTalk, then why are you even here??\n...I mean...I am the FredTranslator after all...")
    print("\nAnyway, you should be glad you've been spared...for now...")
