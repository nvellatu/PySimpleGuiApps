import random


def startGame():
    rounds = int(input("How many rounds would you like in your game?"))
    roundCounter = 0
    choices = ["r", "p", "s"]
    userPoints = 0
    computerPoints = 0
    while ((rounds != 0) and (userPoints-computerPoints<=rounds) and(computerPoints-userPoints<=rounds)):
        roundCounter+=1
        rounds-=1
        userChoice = input("(r) Rock\n(p) Paper\n(s) Scissors\nEnter your choice: ").lower()
        computerChoice = random.choice(["r", "p", "s"])
        print(f"I chose {computerChoice}")

        if userChoice == computerChoice:
            print("Tie!")
        elif userChoice == "r":
            if computerChoice == "p":
                print(f"I win round {roundCounter}!")
                computerPoints+=1
            elif computerChoice == "s":
                print(f"You win round {roundCounter}.")
                userPoints+=1
        elif userChoice == "p":
            if computerChoice =="r":
                print(f"You win round {roundCounter}.")
                userPoints += 1
            elif computerChoice == "s":
                print(f"I win round {roundCounter}!")
                computerPoints += 1
        elif userChoice == "s":
            if computerChoice == "r":
                print(f"I win round {roundCounter}!")
                computerPoints += 1
            elif computerChoice == "p":
                print(f"You win round {roundCounter}.")
                userPoints += 1
        print(f"You - Me : {userPoints} - {computerPoints}")
    if userPoints>computerPoints:
        print("You win...congrats..")
    else:
        print("I WIIINNNNNNN!!!!!!!!!!!!!!")


startGame()
