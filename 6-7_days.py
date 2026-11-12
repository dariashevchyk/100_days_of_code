import random

word_list = ["camel", "apple", "banana", "cherry"]

stages = [
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
]

secret_word = random.choice(word_list)
word_length = len(secret_word)

lives = 6
correct_letters = []
wrong_letters = []

print("_ " * word_length)

game_over = False
while not game_over:
    print(f"\nLives: {lives}")
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Only one letter!.")
        continue

    if guess in correct_letters or guess in wrong_letters:
        print(f"You already mentioned this letter earlier'{guess}'.")
        continue

    if guess in secret_word:
        correct_letters.append(guess)
    else:
        wrong_letters.append(guess)
        lives -= 1
        print(f"Літери '{guess}' немає в слові.")

    display = ""
    for letter in secret_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("You win!")
    elif lives == 0:
        game_over = True
        print(f"You lose! Secret word: {secret_word}")