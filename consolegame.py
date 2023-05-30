print("----------------------------------------------------------")
print("                     COMPUTER RIDDLES")
print("----------------------------------------------------------")
print()
print("----------------------------------------------------------")
print("THESE BRAIN GAMES ARE GUARANTEED TO BOOST YOUR BRAINPOWER.")
print("----------------------------------------------------------")
print("HINT: YOU KNOW ME!")
print("")

answers = ["KEYBOARD", "SPACE", "COMPUTER", "WEBSITE", "CHIPS", "MOUSE", "MONITOR", "INTERNET EXPLORER", "WINDOWS", "DISC-O"]
point = 0

print("1. I Have No Doors But I Have Keys.")
answer1 = input("WHAT'S YOUR ANSWER: ")
if answer1 == answers[0]:
    point += 1
    print("GREAT!")
else:
    print("OH NO!")

print("2. Aliens Favorite Place On A Computer?")
answer2 = input("WHAT'S YOUR ANSWER: ")
if answer2 == answers[1]:
    point += 1
    print("GREAT!")
else:
    print("OH NO!")

print("3. I am in the school or home. I have a mouse. You can use me for work or games. You can use me for email I know! What am I?")
answer3 = input("WHAT'S YOUR ANSWER: ")
if answer3 == answers[2]:
    point += 1
    print("GREAT")
else:
    print("OH NO")

print("4. What did the spider do on the computer?")
answer4 = input("WHAT'S YOUR ANSWER: ")
if answer4 == answers[3]:
    point += 1
    print("GREAT")
else:
    print("OH NO!")

print("5. What Computers eat when they are hungry?")
answer5 = input("WHAT'S YOUR ANSWER: ")
if answer5 == answers[4]:
    point += 1
    print("GREAT!")
else:
    print("OH NO!")

print("6. I have a tail and two flat ears. I move with no feet.")
answer6 = input("WHAT'S YOUR ANSWER: ")
if answer6 == answers[5]:
    point += 1
    print("GREAT!")
else:
    print("OH NO!")

print("7. A box to anywhere. Just watch for my glare.")
answer7 = input("WHAT'S YOUR ANSWER: ")
if answer7 == answers[6]:
    point += 1
    print("GREAT!")
else:
    print("OH NO!")

print("8. I move slower than molasses, if you use me, you probably wear glasses.")
answer8 = input("WHAT'S YOUR ANSWER: ")
if answer8 == answers[7]:
    point += 1
    print("GREAT!")
else:
    print("OH NO!")

print("9. 25 years old, but only turned 10.")
answer9 = input("WHAT'S YOUR ANSWER: ")
if answer9 == answers[8]:
    point += 1
    print("GREAT!")
else:
    print("OH NO!")

print("10. What do computer programmers sing in the shower?")
answer10 = input("WHAT'S YOUR ANSWER: ")
if answer10 == answers[9]:
    point += 1
    print("GREAT!")
else:
    print("OH NO!")

print("Your point is:", point)
