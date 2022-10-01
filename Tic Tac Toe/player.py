import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return random.choice(game.available_moves())

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        while not valid_square:
            square = input(self.letter + "\'s turn. Input move(0-8):")

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

class GeniusComputer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) #random if board's empty
        else:
            #minimax algorithm
            square = self.minimax(game, self.letter)
        return square

    def minimax(self, state, player): # is ran for each possible turn that can take place; it is players turn
        max_player = self.letter    #always me
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player: # case 1: was the previous move a winner?
            return {'position': None,  #i aint making a move when this bitch is empty
                    'score' : 1*(state.num_empty_squares() +1)# if the previous move was me positive score
                    if other_player == max_player else -1*(state.num_empty_squares() +1)}#else negative score

        elif not state.empty_squares(): #case 2: no empty squares/full board/tie
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf} #each following score should be larger
        else:
            best = {'position': None, 'score': math.inf} #each following score should be smaller

        for possible_move in state.available_moves():
            #make a move and try that spot
            state.make_move(possible_move, player)
            #simulate the game after making that move by running minimax again
            sim_score = self.minimax(state, other_player)
            #undo that move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score




