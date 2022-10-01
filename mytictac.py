import random
import time

def printBoard(board):
    for row in [board[i*3: (i+1)*3]for i in range(3)]:
        print('| ' +  ' | '.join(row) + ' |')

def printBoardNums():
    numberBoard = [[str(i+1) for i in range(j*3, (j+1)*3)]for j in range(3)]
    for row in numberBoard:
        print('| ' + ' | '.join(row) + ' |')

def availableSpots(board):
    return [i+1 for i, spot in enumerate(board) if spot == ' ']

def makeHumanMove(board, letter):
    validSpot = False
    while not validSpot:
        print("It is " + letter + "\'s turn.")
        choice = int(input(letter + ", pick a spot on the board. (1-9): "))
        if choice in availableSpots(board):
            board[choice - 1] = letter
            validSpot = True
            time.sleep(.4)
            print("Your move: ")
            printBoard(board)
        else:
            print("Invalid spot")


def checkWinner(board, letter):
    #check rows
    for row in [board[i*3: (i+1)*3]for i in range(3)]:
        if all(spot == letter for spot in row):
            return True

    #check columns
    for row in [[board[i-1]for i in range(1+j, 10, 3)]for j in range(3)]:
        if all(spot == letter for spot in row):
            return True

    #check diagonals
    for diag in [[board[i-1]for i in [1,5,9]],[ board[i-1] for i in [3,5,7]]]:
        if all(spot == letter for spot in diag):
            return True

    return False

def play(computer):
    board = [' ' for i in range(9)]
    printBoardNums()
    if computer:
        while(' ' in board):
            makeHumanMove(board, 'X')
            if checkWinner(board, 'X'):
                print("You won...")
                break


            if availableSpots(board):
                computerChoice = random.choice(availableSpots(board))
                board[computerChoice - 1] = 'O'
                time.sleep(.8)
                print("Computer's turn: ")
                time.sleep(.8)
                printBoard(board)
                if checkWinner(board, 'O'):
                    print("I WONNNN!!!!!!\noh and u lost")
                    break
    else:
        while ' ' in board:
            makeHumanMove(board, 'X')
            if checkWinner(board, 'X'):
                print("Player X has won!")
                break

            makeHumanMove(board, 'O')
            if checkWinner(board, 'O'):
                print("Player O has won!")
                break

        print("It's a tie")




response = input("Do you want to play against me(m) or a friend(f)?")

computer = True if response=='m' else 'f'
play(computer)