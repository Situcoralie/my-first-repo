#THIS IS MY ROCK PAPER SCISSORS GAME

print("Welcome to my game")

player_choice = input("Please select an option from 'rock', 'paper', 'scissors':")
print("USER CHOSE:", player_choice)

#todo: validation step

import random

VALID_OPTIONS = ['rock', 'paper', 'scissors']

computer_choice = random.choice(VALID_OPTIONS)
print("COMPUTER CHOSE:", computer_choice)

print("WINNER: TODO")