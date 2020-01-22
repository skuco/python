import random

random = random.randint(1, 10)
guess = -1
while guess != random:
    guess = int(input('Guess the number: '))
    if guess == random:
        print('Spravne!')
