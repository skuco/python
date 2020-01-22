# Na začiatku sa opýtaj používateľa na meno hráča.
# Počítač si v zápätí bude myslieť náhodné číslo o 1 po 10 (vrátane 1 a 10).
# Opýta sa hráča na jeho tip. Ak hráč uhádne, program si bude myslieť dalšie číslo.
# Ak neuhádne, tak háda to isté číslo dokola až pokým ho neuhádne alebo nezadá "KONIEC".
# Po ukončení hry sa vypíšu základné štatistiky ako počet správnych, počet nesprávnych a celkový počet tipov.

import random

print("___  ___          _           ___  ____           _ \n"
      "|  \/  |         | |          |  \/  (_)         | |\n"
      "| .  . | __ _ ___| |_ ___ _ __| .  . |_ _ __   __| |\n"
      "| |\/| |/ _` / __| __/ _ \ '__| |\/| | | '_ \ / _` |\n"
      "| |  | | (_| \__ \ ||  __/ |  | |  | | | | | | (_| |\n"
      "\_|  |_/\__,_|___/\__\___|_|  \_|  |_/_|_| |_|\__,_|\n")
                                                
name = input("Enter your name: ")
if name == "":
    name = "player"

print("\nHi, " + name + ". Here are the rules.\n"
      "I will think the random number from 1 to 10.\n"
      "You, " + name + " will guess it.\n"
      "You can guess how many rounds you want.\n"
      "Just type 'FINISH' and I will quit the game and show you the score.\n"
      "Good luck, " + name + ".\n")

print("Okay, I'm thinking the number...")
rand_number = random.randint(1, 10)
guess = -1
correct_guess = 0
wrong_guess = 0

while True:
    guess = input("Guess the number: ")
    wrong_guess += 1
    game_over = "finish"
    if guess == str(rand_number):
        print("Correct!")
        correct_guess += 1
        rand_number = random.randint(1, 10)
    elif game_over == guess.lower().strip():
        wrong_guess -= 1
        break

#print("Correct guess: {}\nWrong guess: {}\nTotal: {}".format(correct_guess, wrong_guess - 1, (correct_guess + wrong_guess)-1))

print("+{:-^24}+".format("Your Score"))
print("|{0:>12}{1:<12}|".format("Correct: ", correct_guess))
print("|{0:>12}{1:<12}|".format("Incorrect: ", wrong_guess - 1))
print("|{0:>12}{1:<12}|".format("Total: ", (correct_guess + wrong_guess)-1))
print("+{:-^24}+".format("-"))