import random
# 1 part
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# option 1
print(random.choice(friends))
# option 2
random_index = random.randint(0, len(friends)-1)
print(friends[random_index])

# 2 part
people_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))
computer_choice = random.randint(0,2)

if people_choice == 0:
    print("You chose Rock")
elif people_choice == 1:
    print("You chose Paper")
elif people_choice == 2:
    print("You chose Scissors")
else:
    print("You chose a wrong option")
    exit()

if computer_choice == 0:
    print("Computer chose Rock")
elif computer_choice == 1:
    print("Computer chose Paper")
else:
    print("Computer chose Scissors")

if computer_choice == people_choice:
    print("No winners! It`s a draw")
elif computer_choice == 0 and people_choice == 2:
    print("You lose!")
elif people_choice > computer_choice:
    print("You win!")
elif computer_choice == 0 and people_choice == 1:
    print("You win!")
elif computer_choice > people_choice:
    print("You lose!")

