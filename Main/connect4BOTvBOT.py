import os
import csv
import time
import random

BOARD_COLS = 7
BOARD_ROWS = 6

scoreboard = open("Main\scoreboard.csv", "a")
playersName = ["BotOne", "BotTwo"]

class Board():
    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        self.turns = 0
        self.last_move = [-1, -1] 

    def print_board(self):
        print("\n")
        
        for r in range(BOARD_COLS):
            print(f"  ({r+1}) ", end="")
        print("\n")

       
        for r in range(BOARD_ROWS):
            print('|', end="")
            for c in range(BOARD_COLS):
                print(f"  {self.board[r][c]}  |", end="")
            print("\n")

        print(f"{'-' * 42}\n")

    def which_turn(self):
        players = ['X', 'O']
        return players[self.turns % 2]
    
    def in_bounds(self, r, c):
        return (r >= 0 and r < BOARD_ROWS and c >= 0 and c < BOARD_COLS)

    def turn(self, column):
      
        for i in range(BOARD_ROWS-1, -1, -1):
            if self.board[i][column] == ' ':
                self.board[i][column] = self.which_turn()
                self.last_move = [i, column]

                self.turns += 1
                return True

        return False

    def check_winner(self):
        last_row = self.last_move[0]
        last_col = self.last_move[1]
        last_letter = self.board[last_row][last_col]

       
        directions = [[[-1, 0], 0, True], 
                      [[1, 0], 0, True], 
                      [[0, -1], 0, True],
                      [[0, 1], 0, True],
                      [[-1, -1], 0, True],
                      [[1, 1], 0, True],
                      [[-1, 1], 0, True],
                      [[1, -1], 0, True]]
        
        
        for a in range(4):
            for d in directions:
                r = last_row + (d[0][0] * (a+1))
                c = last_col + (d[0][1] * (a+1))

                if d[2] and self.in_bounds(r, c) and self.board[r][c] == last_letter:
                    d[1] += 1
                else:
                   
                    d[2] = False

       
        for i in range(0, 7, 2):
            if (directions[i][1] + directions[i+1][1] >= 3):
                os.system('cls')
                self.print_board()
                print(f"{last_letter} is the winner!")

                scoreboard = open("Main\scoreboard.csv", "r")
                reader = csv.reader(scoreboard)
                rows = list(reader)

                numX = rows[0][1]
                numO = rows[1][1]

                scoreboard.close()

                scoreboard = open("Main\scoreboard.csv", "w")
                if last_letter == "X":
                    numX = int(numX) + 1
                    new = "X" + "," + str(numX) + "\n" + "O" + "," + str(numO)
                if last_letter == "O":
                    numO = int(numO) + 1
                    new = "X" + "," + str(numX) + "\n" + "O" + "," + str(numO)
                scoreboard.write(str(new))

                return last_letter   

       
        return False

def play():
   
    game = Board()

    game_over = False
    while not game_over:
        os.system("cls")
        game.print_board()

       
        valid_move = False
        while not valid_move:
            currentPlayer = game.which_turn()
            if currentPlayer == "X":
                currentPlayer = playersName[0]
                user_move = random.randint(0,6)
                user_move = user_move + 1
                print(f"{currentPlayer} Is Playing")
                time.sleep(2)
            else:
                currentPlayer = playersName[1]
                user_move = random.randint(0,6)
                user_move = user_move + 1
                print(f"{currentPlayer} Is Playing")
                time.sleep(2)
            try:
                valid_move = game.turn(int(user_move)-1)
            except:
                print(f"Please choose a number between 1 and {BOARD_COLS}")

        
        game_over = game.check_winner()
        
        
        if not any(' ' in x for x in game.board):
            print("The game is a draw..")
            return


if __name__ == '__main__':
    play()
  