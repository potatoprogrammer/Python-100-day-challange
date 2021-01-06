from art import logo

print(logo)

print("Welcome to the number guessing game!")

import random

the_number = random.randint(1,101)

print("for testing purpose, the answer is: "+the_number)

dificulty = input("Chose a dificulty. Type 'easy' or 'hard': ").lower()

attempts = 0

if dificulty == "easy":
  attempts = 10
else:
  attempts = 5

game_over = False

while not game_over:
  if attempts < 1:
    game_over = True

  print(f"You have {attempts} remaining to guess the number.")

  guess = int(input("Make a guess: "))

  if guess > the_number:
    print("Too high")
    print("Guess again.")
    attempts -= 1
  elif guess < the_number:
    print("Too low")
    print("Guess again")  
    attempts -= 1
  else:
    print("You win!")
    game_over = True  