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
    name = input("What's your name ?")

    curr_time = datetime.now()
    morning_wishes = ["Good day to you!","Rise and shine!","Wakey-wakey!","Morning, good looking!"]
    noon_wishes = ["Thinking of you today — have a good afternoon!","Have a good afternoon and a great day!","Enjoy this time of day","Wishing you a splendid afternoon my one and only!"]
    evening_wishes = ["Very Fine evening","Good evening Buddy"]
    night_wishes = ["How was your day ?","It's late"]
    symbojis = ["   ɾ⚈▿⚈ɹ   ","   」(￣▽￣」)   ","   ☜(⌒▽⌒)☞   "]
    symboji = random.choice(symbojis)
    time_of_day_greeting = random.choice(morning_wishes)

    if(curr_time.hour > 12 and curr_time.hour <17):
        time_of_day_greeting = random.choice(noon_wishes)
    elif(curr_time.hour >17 and curr_time.hour <22):
        time_of_day_greeting = random.choice(evening_wishes)
    elif(curr_time.hour >22):
        time_of_day_greeting = random.choice(night_wishes)

    print(time_of_day_greeting,name,symboji,"\n")

def drop_menu():
    print(" Are you getting bored ? wanna do something    （‐＾▽＾‐）       .......   \n")
    print("What do you wanna do : \n")
    print(" 1. Perform some calculation.")
    print(" 2. Play rock paper scissors    (≧∇≦*)  .\n")
    print(" 3. End the chat. ")
    print(" Choose an option : ")

def inp():
    try:
        choice = int(input())
        return choice
    except:
        return 0


def calculations():
    expression = input("enter an expression : ")
    try:
        print("Answer is : ",eval(expression)) 
    except Exception as e:
        print(str(e))

def rock_pap_sis():
    print(" Entering the game   ......\n")
    print( "Instructions : \n")
    print(" Press R for Rock.")
    print(" Press P for Paper.")
    print(" Press S for Scissor.")
    print("\n Who first gets 5 points is the winner.\n ")
    print(" Your choice   ( ͡° ͜ʖ ͡°)  : ")
    entries = ["R","P","S"]
    bot_points = 0
    user_points = 0
    while(bot_points<5 and user_points<5):
        choice = input("Enter your choice : ")
        if(choice not in entries):
            print("\n You entered the wrong one")
            print("Enter only R ,P or s")
        else:
            play(choice,bot_points,user_points)
    if(bot_points > user_points):
        print(" (✖╭╮✖)  (✖╭╮✖)  You Lost  (✖╭╮✖)  (✖╭╮✖)")
        print(" You lost the Game by ",(bot_points-user_points))
    else:
        print(" (◍•ᴗ•◍)❤   (◍•ᴗ•◍)❤   You Won  (◍•ᴗ•◍)❤  (◍•ᴗ•◍)❤")

def play(choice,bot_points,user_points):
    entries = ["R","P","S"]
    bot = random.choice(entries)
    if(choice == "R"):
        if(bot == "R"):
            print("You : Rock  Playbot : Rock")
            print("Draw")
            print("Your points : ",user_points,"\n My points : ",bot_points)
        elif(bot == "P"):
            print("You : Rock  Playbot : Paper")
            print("Bad Choice   ಠ╭╮ಠ")
            bot_points+=1
            print("Your points : ",user_points,"\n My points : ",bot_points)
        else:
            print("You : Rock  Playbot : Scissor")
            print("Good Job   (◑‿◐)")
            user_points+=1
            print("Your points : ",user_points,"\n My points : ",bot_points)
    elif(choice == "P"):
        if(bot == "P"):
            print("You : Paper  Playbot : Paper")
            print("Draw")
            print("Your points : ",user_points,"\n My points : ",bot_points)
        elif(bot == "S"):
            print("You : Paper  Playbot : Scissor")
            print("Bad Choice   ಠ╭╮ಠ")
            bot_points+=1
            print("Your points : ",user_points,"\n My points : ",bot_points)
        else:
            print("You : Paper  Playbot : Rock")
            print("Good Job   (◑‿◐)")
            user_points+=1
            print("Your points : ",user_points,"\n My points : ",bot_points)
    else:
        if(bot == "P"):
            print("You : Scissor  Playbot : Paper")
            print("Good Job   (◑‿◐)")
            user_points+=1
            print("Your points : ",user_points,"\n My points : ",bot_points)
        elif(bot == "S"):
            print("Draw")
            print("Your points : ",user_points,"\n My points : ",bot_points)
        else:
            print("You : Scissor  Playbot : Rock")
            print("Bad Choice   ಠ╭╮ಠ")
            bot_points+=1
            print("Your points : ",user_points,"\n My points : ",bot_points)

def playbot():
    intro()
    wishes()
    drop_menu()
    choice = inp()
    while (choice != 3):
        if(choice == 1):
            calculations()
        elif(choice == 2):
            rock_pap_sis()
        else:
            print("I don't understand.  ヽ༼⊙_⊙༽ﾉ  ")
            print("Please enter only 1 or 2  or 3")
        drop_menu()
        choice = inp()
    if(choice == 3):
        print("Nice talking to you. ________  ʕ ▀ ڡ ▀ ʔ  ʕ ▀ ڡ ▀ ʔ  __________")


playbot()











