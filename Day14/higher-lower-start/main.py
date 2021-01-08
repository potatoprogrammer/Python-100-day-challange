import random
from art import logo, vs
from game_data import data
import os

print(logo)

def gen_number():
  rand_number = random.randint(0,len(data) - 1)
  return rand_number
score = 0
end_game = False

while not end_game:
  if score > 0:
    print(f"You're right! Current score: {score}.")

  rand_num1 = gen_number()
  option_a = data[rand_num1]['follower_count']
  print(f"Compare A: {data[rand_num1]['name']}, a {data[rand_num1]['description']}, from {data[rand_num1]['country']}.")

  rand_option = gen_number()
  if rand_option == rand_num1:
    rand_option = rand_num1 - 1

  print(vs)

  option_b = data[rand_option]['follower_count']
  answer = 0
  answer_option = ""
  if option_b > option_a:
    answer = option_b
    answer_option = "b"
  else:
    answer = option_a  
    answer_option = "a"

  user_answer = input(f"Against B: {data[rand_option]['name']}, a {data[rand_option]['description']}, from {data[rand_option]['country']}.\n Who has more followers? Type 'A' or 'B': ").lower()

  if user_answer == answer_option:
    score += 1
    os.system("clear")    
  else:
    os.system("clear")
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")  
    score = 0  
    end_game = True  