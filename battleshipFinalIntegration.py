# Luke Preston
"""This program is designed to be a similar replication of the well known game
"Battleship".
The program will correctly be able to take your guess of where you think the
opponents enemy ship is and will give you a "HIT!" or "MISS" response.
If you are finally able to sink your opponents battleship, the game will
finish and you will have won!"""


# Introduction
# Function that receives Player Name
player_name = input("Please enter your first name to get started. ")
print("Fleet Admiral Wilson: Welcome aboard", player_name + "!")

# Gather player experience
"""
* If yes player may skip practice level
* If no player must go through practice level 
"""
while True:
  player_experience  = input("Fleet Admiral Wilson: Have you played battleship"
                             " before? Enter yes/no : ")
  if player_experience  == "yes":
    print("Fleet Admiral Wilson: Great!", " We need more soilders like you if"
                                    " we're going to win this war.", sep="-->")
    """ sep="-->" gets rid of the whitespace in between the two strings 
and places the arrow within the quotes """
    break
  elif player_experience == "no":
    print("Fleet Admiral Wilson: Well Private we've got some learning to do!"
          " The goal of the game is to sink the enemies battleship!")
    break
  else:
    print("Error. Make sure you enter either yes or no.")

# Testing your sea legs
while True:
  sea_sickness = (input("Fleet Admiral Wilson: Do you get sea sick easily son?"
                        " Enter yes/no : "))
  if sea_sickness == "yes":
    print("Fleet Admiral Wilson: You're going to have to toughen up Private!"
          " Because we're going to the roughest of seas!"
          " Now drop and give me 20!")
    break
  elif sea_sickness == "no":
    print("Fleet Admiral Wilson: Well it dosen\'t matter Private!"
          " Because we're headed straight towards the roughest of seas!")
    break
  else:
    print("Error. Make sure you enter either yes or no.")

print()
print("Fleet Admiral Wilson: We will go over the official rules very soon.")
print("Fleet Admiral Wilson: For now, let's pick what team you"
      " would like to be on.")

# Red or Blue Team <<<<
while True:
  team_color = input("Please pick your team. Enter Red or Blue: ")
  if (team_color == "Red"):
    print(" ")
    print("Fleet Admiral Wilson: Nice choice", player_name + ".", "You will be"
                            " going against your arch rivals, the Blue Team.")
    break
  elif (team_color == "Blue"):
    print()
    print("Fleet Admiral Wilson: Great pick", player_name + ".", "You will be"
                            " going against your arch rivals, the Red Team.")
    break
  else:
    """ The int(3) prints the "Error" message three times because it
     is being multiplied """
    print("Error! " * int(3), "Make sure your spelling is correct.")

load_gameboard = input("Press any key to load the game board: ")

x = "LETS BEGIN:"
print(x, end=" ")
print("Fleet Admiral Wilson: Now that you\'re all set up, let\'s show"
      " you the game board!")
print()
number = 0
while (number < 100) and (number >= 0):
  number = number + 1
  print("Loading:", number, "%")
print("Finished.")
print()

""" The print_board variable holds the string "o" and multiplies that 
string by 5.While being introduced to the range function that creates 5 rows. 
 Therefore creating a 5x5 game board which is exactly what we want. """

# Function that prints layout of the board
board = []

for i in range(0, 5):
    board.append(["o"] * 5)


def print_board(board):
    for row in board:
        print((" ").join(row))


print_board(board)

print()


# Game board instructions
print("Fleet Admiral Wilson: This is where you will " + "guess your strikes!")

# The + joins the two strings together in this example
print(
    "Fleet Admiral Wilson: As you can see this is a 5x" + "5 game board, "
    "there are 25 different spots the enemy may be hiding.")
print()
print(
    "Fleet Admiral Wilson: You will go about guessing by choosing "
    "horizontally (by the columns) first, counting from the top left 0.")
print()
print(
    "Fleet Admiral Wilson: From there you will be able to guess "
    "vertically (by the rows), counting from the top of your horizontal "
    "guess to the bottom of the board.")
print()
print(
    "Fleet Admiral Wilson: You only get 10 guesses to find the enemy ship, if "
    "you fail to do so, you lose. If you do sink the ship in under 10 or "
    "less guesses, congratulations! You win!")
print()
print(
    "Fleet Admiral Wilson: Now that you know the rules Private, we can "
    "get started! Fire Away!")

print()

print("Our headquarters has contacted us with radar signals in these "
      "3 columns for level 1. Still our surveillance can be wrong.")

""" *The % checks to see if there is a remainder equal to 1 to make 
sure that it prints an odd number 
    * The sep function fills in the white space between the variable 
and the empty quotes with a string """

for number in range(1, 6):
    if (number % 2 == 1):
        print(number, " ", sep=" <-- Radar signaled this column")
        print()

# Random number generator for the user to try and guess
from random import randint

print_board(board)

print()

def random_row(board):
    return (randint(0, len(board) - 1))


def random_col(board):
    return (randint(0, len(board) - 1))


ship_row = random_row(board)
ship_col = random_col(board)

print()


def main():
    num_of_guess = 1
    while (num_of_guess):
        guess_col = int(input("Guess column: "))
        guess_row = int(input("Guess row: "))
        num_of_guess += 1
        if (guess_col == ship_col and ship_row == ship_row):
            print("Hit! You Sunk the enemies Battleship!")
            board[guess_row][guess_col] = "*"
            print_board(board)
            print("Guesses Taken: ", num_of_guess)
            print()
            print('GAME OVER! YOU\'VE WON!')
            break
        elif (guess_col >= 5 or guess_row >= 5):
            print("Your guess is invalid, make sure your guess "
                  "is on the board.")
            print("Guesses Left: ", 11 - num_of_guess)
        elif board[guess_row][guess_col] == "X":
            print("You have already guessed that area.")
            print("Guesses Left: ", 11 - num_of_guess)
        elif (num_of_guess > 11):
            print("Game over. You have run out of guesses.")
            print_board(board)
            break
        else:
            print("You missed the enemy battleship.")
            board[guess_row][guess_col] = "X"
            print_board(board)
            print("Guesses Left: ", 11 - num_of_guess)
            print('GAME OVER.')
main()












