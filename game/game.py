from random import randint

while True:
    try:

        sath = int(input("Level: "))
        if sath > 0:
            break
    except ValueError:
        pass


random = randint(1, sath)

while True:
    try:

        hads = int(input("Guess: "))
        if hads <= 0:
            continue
    except ValueError:
        continue


    if hads > random:
        print("Too large!")
    elif hads < random:
        print("Too small!")
    else:
        print("Just right!")
        break