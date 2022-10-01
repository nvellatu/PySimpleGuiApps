from words import words
import random
def startGame():
    word = getComputerWord()
    mistakesAllowed = 5
    lettersFound = ""
    lettersTried = []
    for letter in word:
        if letter == " ":
            lettersFound += " "
        elif letter == "-":
            lettersFound += "-"
        else:
            lettersFound += "_"
    wordFound = False
    while (mistakesAllowed > 0) and not (wordFound):
        print("Here are the letters you have found: ")
        print(lettersFound)
        print("Letters Tried: " + ", ".join(lettersTried))
        print(f"You have {mistakesAllowed} more mistakes allowed.")
        guess = input("Enter your guess: ").upper()
        if len(guess) <= len(word):
            found = False
            for i in range(0, len(word) - len(guess)+1):
                if word[i: i + len(guess)] == guess:
                    lettersFound = list(lettersFound)
                    for j in range(i, i + len(guess)):
                        lettersFound[j] = guess[j - i]
                    lettersFound = "".join(lettersFound)
                    found = True
            lettersTried.append(guess)
            if not found:
                print("That letter was not in there.")
                mistakesAllowed -= 1
        else:
            print("That letter was not in there.")
            mistakesAllowed -= 1
        if lettersFound == word:
            wordFound = True
    if wordFound:
        print("Congrats you won!!!")
        print("the word was: ".upper() + word)
    else:
        print("haha you lost")
        print("the word was: " + word)


def getUserWord():
    return input("Enter the word, or sentence for Hangman: ").upper()


def getComputerWord():
    return random.choice(words).upper()


startGame()