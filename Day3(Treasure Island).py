print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome To Treasure Island.")
print("Your mission is to find the treasure")
first=input('You\'re at a cross road. Where do you want to go? Type "left" or "right"')
if first == "left":
    second=input('You come at a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Types "swim" to swim across')
    if second == "wait":
        third=input('You arrive at the island unharmed. There is a house with 3 doors. One "red", one "yellow" and one "blue". Which colour do you choose?.')
        if third == "red":
            print("Burned by fire.GAME OVER.")
        elif third == "blue":
            print("Eaten by beast.GAME OVER.")
        elif third == "yellow":
            print("You WIN!")
        else:
            print("GAME OVER")
    else:
        print("Attacked by trout.GAME OVER")
else:
    print("You fell into a hole. GAME OVER.")