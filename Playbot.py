'''

Chatbot program
. starts with intro 
. asks for name 
. and wishes the user
. drops a menu and asks the user to choose an option he/she wants
. and responds according to the user input


'''

import random
from datetime import datetime

def intro():
    # declaring a set of intro responses
    intros = [
        "Hi my name is playbot   ᵔᴥᵔ","You can play with me.   ʕ•ᴥ•ʔ","Nice to see you.   [⑇◍ᴥ◍•⑇]"," Hey,how do you do    ƪ(˘⌣˘)ʃ"
    ]
    print("\n",random.choice(intros),"\n")


def wishes():
    #asking for the name of the user
    name = input(" What's your name ?")
    #for getting the current time
    curr_time = datetime.now()
    morning_wishes = ["Good day to you!","Rise and shine!","Wakey-wakey!","Morning, good looking!"]
    noon_wishes = ["Thinking of you today — have a good afternoon!","Have a good afternoon and a great day!","Enjoy this time of day","Wishing you a splendid afternoon my one and only!"]
    evening_wishes = ["Very Fine evening","Good evening Buddy"]
    night_wishes = ["How was your day ?","It's late"]
    symbojis = ["   ɾ⚈▿⚈ɹ   ","   」(￣▽￣」)   ","   ☜(⌒▽⌒)☞   "]
    symboji = random.choice(symbojis)
    time_of_day_greeting = random.choice(morning_wishes)
    #deciding the time of the day
    if(curr_time.hour > 12 and curr_time.hour <17):
        time_of_day_greeting = random.choice(noon_wishes)
    elif(curr_time.hour >17 and curr_time.hour <22):
        time_of_day_greeting = random.choice(evening_wishes)
    elif(curr_time.hour >22):
        time_of_day_greeting = random.choice(night_wishes)

    print("\n ",time_of_day_greeting,name,symboji,"\n")

def drop_menu():
    print(" Are you getting bored ? wanna do something    （‐＾▽＾‐）       .......   \n")
    print("What do you wanna do : \n")
    print(" 1. Perform some calculation.")
    print(" 2. Play rock paper scissors    (≧∇≦*)  .")
    print(" 3. End the chat. \n")
    print("___________________________________________________________")
    print(" Choose an option : ")

def inp():
    try:
        choice = int(input())
        return choice
    except:
        return 0


def calculations():
    expression = input("\n\nEnter an expression : ")
    try:
        print("\nAnswer is : ",eval(expression),"\n") 
    except Exception as e:
        print(str(e),"\n")

def rock_pap_sis():
    print(" Entering the game   ......\n")
    print( "Instructions : \n")
    print(" Press R for Rock.")
    print(" Press P for Paper.")
    print(" Press S for Scissor.")
    print("\n Who first gets 5 points is the winner.\n ")
    print(" Press E if you want to exit the game any time.\n")
    print(" Your choice   ( ͡° ͜ʖ ͡°)  : ")
    bot_entries = ["R","P","S"]
    user_entries = ["R","P","S","E"]
    botpoints = 0
    userpoints = 0
    while (botpoints<5 and userpoints<5):
        choice = input("Enter your choice : ")
        if (choice not in user_entries):
            print("\n You entered the wrong one")
            print("Enter only R ,P, S or E")
            continue
        bot = random.choice(bot_entries)
        if choice == "E":
            return 0
        if (choice == "R"):
            if (bot == "R"):
                print("You : Rock  Playbot : Rock")
                print("Draw")
                print("Your points : ",userpoints,"\n My points : ",botpoints)
            elif (bot == "P"):
                print("You : Rock  Playbot : Paper")
                print("Bad Choice   ಠ╭╮ಠ")
                botpoints+=1
                print("Your points : ",userpoints,"\n My points : ",botpoints)
            else:
                print("You : Rock  Playbot : Scissor")
                print("Good Job   (◑‿◐)")
                userpoints+=1
                print("Your points : ",userpoints,"\n My points : ",botpoints)
        elif (choice == "P"):
            if (bot == "P"):
                print("You : Paper  Playbot : Paper")
                print("Draw")
                print("Your points : ",userpoints,"\n My points : ",botpoints)
            elif (bot == "S"):
                print("You : Paper  Playbot : Scissor")
                print("Bad Choice   ಠ╭╮ಠ")
                botpoints+=1
                print("Your points : ",userpoints,"\n My points : ",botpoints)
            else:
                print("You : Paper  Playbot : Rock")
                print("Good Job   (◑‿◐)")
                userpoints+=1
                print("Your points : ",userpoints,"\n My points : ",botpoints)
        else:
            if (bot == "P"):
                print("You : Scissor  Playbot : Paper")
                print("Good Job   (◑‿◐)")
                userpoints+=1
                print("Your points : ",userpoints,"\n My points : ",botpoints)
            elif (bot == "S"):
                print(" You : Scissor  PlayBot : Scissor")
                print("Draw")
                print("Your points : ",userpoints,"\n My points : ",botpoints)
            else:
                print("You : Scissor  Playbot : Rock")
                print("Bad Choice   ಠ╭╮ಠ")
                botpoints+=1
                print("Your points : ",userpoints,"\n My points : ",botpoints)
    if (botpoints > userpoints):
       print("\n\n\n\n\n (✖╭╮✖)  (✖╭╮✖)  You Lost  (✖╭╮✖)  (✖╭╮✖)")
       print(" You lost the Game by ",(botpoints-userpoints),"\n\n\n")
    else:
       print("\n\n\n\n (◍•ᴗ•◍)❤   (◍•ᴗ•◍)❤   You Won  (◍•ᴗ•◍)❤  (◍•ᴗ•◍)❤\n\n\n")
       print(" You won the Game by ",(userpoints-botpoints),"\n\n\n")


def playbot():
    intro()
    wishes()
    drop_menu()
    choice = inp()
    while (choice != 3):
        if(choice == 1):
            calculations()
            print("-------------------------------------------------------------------------------")
        elif(choice == 2):
            rock_pap_sis()
            print("-------------------------------------------------------------------------------")
        else:
            print(" ヽ༼⊙_⊙༽ﾉ   (⊙_☉)  I don't understand.  (⊙_☉)  ヽ༼⊙_⊙༽ﾉ  ")
            print("Please enter only 1 or 2  or 3")
        drop_menu()
        choice = inp()
    if(choice == 3):
        print("\n\n(_______  ｡♥‿♥｡)   乂❤‿❤乂    Nice talking to you   乂❤‿❤乂  (｡♥‿♥｡) _________\n\n")


playbot()
