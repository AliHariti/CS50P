import random


while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

toguess = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < toguess:
            print("Too small!")
        elif guess > toguess:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
