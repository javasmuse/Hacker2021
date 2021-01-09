#!/usr/bin/env python3
import time
import crayons

# create a customizable player


def welcome():
    print("\nYou see a blank screen. It blinks a few times. Then in the center appears: \n")
    login = ""
    round = 0
    while round < 3 and login != "sassycat":
        login = input("Login: ").strip().lower()
        round += 1
        if login == "sassycat":
            print("you found the password!")
        elif round == 3:
            print("\n Third try - Sorry Locked Out - Try ...")
            time.sleep(2)
            print("\n bugs... bugs... bugs... Is it a bug or a feature? .... \n instead of being locked out, the system put you through to the mainframe ")
    mainframe()


def mainframe():
    print("\nYour computer screen displays this message: \n")
    print(crayons.blue("MAGMA LTD. - Interal System Bulletins\n"))
    print(crayons.red("TOP SECRET - World Domination Plans have been relocated for security. One page has been sent to an agent in each of our affiliated countries.\n"))
    time.sleep(3)
    print("Hmmm, you think, wasn't their a reward for thwarting evil plans? How can I get those? \n Further down the screen you notice: \n")
    time.sleep(3)
    print(crayons.blue("The travel droid is fully charged.\n"))
    time.sleep(3)
    print("What would you like to do? \n Enter 1 - get out of here it could be dangerous \n Enter 2 - click on travel droid")
    while True:
        action = input(crayons.blue("> ")).strip()
        if action == "1":
            print(
                "Good thinking those agents could be dangerous. Maybe go play a safer game like Mario. Goodbye")
            break
        elif action == "2":
            print("Excellent choice - your adventure begins!!")
            travelDroid()
            break
        elif action != "2" and action != "1":
            action = input(crayons.blue("> ")).strip()


def travelDroid():
    print(crayons.blue("Hello, I'm a travel droid. I travel underground at the speed of light through special MAGMA LTD. designed tunnels. My charge is good for three hours. I'm also able to impersonate a MAGMA LTD. official. I may be useful in recovering the plans.\nSimple use instruction: to Move: type go with a direction, to Get: type get with an object. \ni.e. go Japan OR get jade"))

def showStatus():
    print(crayons.blue('--------------------------'))
    print(crayons.blue('You are in ' + currentLocale))
    # print players inventory
    print(crayons.blue("Your inventory includes: " + str(inventory)))
    # print an item if there is one in the room
    if "item" in locales[currentLocale]:
        print(crayons.blue("You see a " + locales[currentLocale]['item']))
    print(crayons.blue('--------------------------'))


# PLAYERS INVENTORY
inventory = ["Bitcoin"]

# DICTIONARY LINKING LOCALES TO OTHER LOCALES
locales = {
    'Japan': {
        'east': 'Germany',
        'west': 'Russia',
        'item': 'mini-droid'
    },
    'Russia': {
        'east': 'Japan',
        'south': 'China',
        'item': 'caviar'
    }, 
    'China' : {
        'north' : 'Russia',
        'west' : 'Germany',
        'item' : 'jade'
    }, 
    'Germany' : {
        'east' : 'Japan',
        'west' : 'Russia',
        'item' : 'beer'
    }
}

currentLocale = "Germany"

welcome()

# FOREVER BEGIN
while True:
    showStatus()

    # GET PLAYERS ACTION CHOICE
    move = ''
    while move == '':
        move = input(crayons.blue('> '))

    # split allow items to have a space - it removes the space and takes each word as an element, we want the secone one or idx 1
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check their move is possible from current locale
        if move[1] in locales[currentLocale]:
            # set the current locale to the new locale
            currentLocale = locales[currentLocale][move[1]]
        # if there is no portal to the entered locale
        else:
            print(crayons.blue("Sorry that is not an option. The tunnels are amazing, but the lines are limited as yet."))

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is one they want to get
        if "item" in locales[currentLocale] and move[1] in locales[currentLocale]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(crayons.blue("Got it! The "))
            # delete the item from the room
            del locales[currentLocale]['item']
        # otherwise if the item isn't there to get
        else:
            # tell them they can't get it
            print(crayons.blue(f"The {move[1]} is not here."))

        # Define how a player can win
    if len(inventory) == 5:
        print(crayons.green("You Win - You saved the world from MAGMA LTD. dominiation!!! :) :) :) :) "))
        break
