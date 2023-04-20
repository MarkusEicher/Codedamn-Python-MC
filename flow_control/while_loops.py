""" def fire():
    print("You decide how many times to fire the cannons.")
    rounds = int(input("How many rounds? "))

    while rounds:
        print("You fire the cannons! " + str(rounds) + " times.")
        rounds -= 1

fire() """

""" def fire(rounds):
    # print("You decide how many times to fire the cannons.")
    # rounds = int(input("How many rounds? "))

    while rounds:
        print("You fire the cannons! 🔥")
        rounds -= 1
    print("You need to reload the cannons.")
            

fire(5) """

""" def fire(rounds):
    # print("You decide how many times to fire the cannons.")
    # rounds = int(input("How many rounds? "))

    while True:
        if rounds:
            print("You fire the cannons! 🔥")
            rounds -= 1
        else:
            print("You need to reload the cannons.")
            break
fire(5) """

counter = 0

while counter != 6:
    counter += 1

    if (counter % 2) != 0:
        continue
    else:
        print(counter)