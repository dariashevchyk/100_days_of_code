"First project of day 3"

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
print(f"Your total bill is {bill}")

"Second project"
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
side = input("you are at the cross road. Where do you want to go?\n   Type 'left' or 'right'").lower()
if side == 'left':
    action = input("Your\'ve come to the lake.\n Choose 'swim' to swim across or 'wait' to wait for the boat").lower()
    if action == 'wait':
        door= input("You arrive at the island unharmed.\n There is house with 3 doors.\n Which door do you want to choose? Red, Yellow or Blue").lower()
        if door == 'red':
            print("It`s a room full of fire. Game Over")
            exit()
        elif door == 'yellow':
            print("You find a treasure! You win!")
            exit()
        elif door == 'blue':
            print("Eaten by beasts. Game Over")
            exit()
        else:
            print("Game Over")
            exit()
    else:
        print("You were attacked by trout. Game over.")
        exit()
else:
    print("Fall into a hole. Game Over")
    exit()