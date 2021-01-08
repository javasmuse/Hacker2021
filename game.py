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
            print("\n bugs... bugs... bugs... Is it a bug or a feature? .... \n instead of being locked out the system put you through. ")
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


# PLAYERS INVENTORY
inventory = []

# DICTIONARY LINKING LOCALES TO OTHER LOCALES
locales = {
    'Japan': {
        'south': 'China',
        'west': 'Russia',
        'item': 'small fun droid'
    },

    'Russia': {
        'east': 'Japan',
        'west': 'Germany',
        'item': 'caviar'
    }

}


welcome()
