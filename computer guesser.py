def computer_guess():
    low = isLowerThan(1)
    high = isHigherThan(10)
    print("Your number is " + str(guesser(low, high)))


def isLowerThan(low):
    if (input("Is your number lower than " + str(low) + "? (yes or no)").lower() == "no"):
        return low
    else:
        if low > 0:
            low *= -1
        return isLowerThan(low * 10)


def isHigherThan(high):
    if (input("Is your number higher than " + str(high) + "? (yes or no)").lower() == "no"):
        return high
    else:
        return isHigherThan(high * 10)


def guesser(low, high):
    mid = int((low + high) / 2)
    answer = input(
        "Is your number lower than, higher than, or equal to " + str(mid) + "? (lower, higher, or equal)").lower()
    if answer == "lower":
        high = mid
        return guesser(low, high)
    elif answer == "higher":
        low = mid
        return guesser(low, high)
    else:
        return mid


def computer_guess2():
    counter = 0
    low = 0
    high = 0
    guess =100
    if input("Is your number positive?(yes or no)").lower() == "no":
        guess= -100
        a=True
    a=False
    feedback = ""
    while feedback != "e":
        counter+=1
        feedback = input(f"Is your number equal to (e), less than (l), or greater than (g) {guess}?")
        if a:
            if feedback == "g":
                high = guess
                guess = int((high + low) / 2)
            elif feedback == "l":
                low = guess
                if high == 0:
                    guess *= 2
                else:
                    guess = int((high + low) / 2)
        else:
            if feedback == "l":
                high = guess
                guess = int((high + low) / 2)
            elif feedback == "g":
                low = guess
                if high == 0:
                    guess *= 2
                else:
                    guess = int((high + low) / 2)
    print(f"In {counter} guesses I found that your number is {guess}")


computer_guess2()
