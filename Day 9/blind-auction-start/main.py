from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
more = True
bids = {}
while more:
  print(logo)
  print("Welcome to the secret auction program.")
  #print("What is your name?: ")
  name = input("What is your name: ")
  #print("What's your bid?: ")
  person_bid = int(input("What's your bid: $"))
  more_bidders = input("Are there any other biddrs? Type 'yes' or 'no'.\n").lower()

  bids[name] = person_bid
  clear()

  if more_bidders == "no" or more_bidders == "n":
    more = False

highest_bid = 0
highest_bidder = ""
for key in bids:
  if bids[key] > highest_bid:
    highest_bid = bids[key]
    highest_bidder = key

print(bids)
print(f"The winner of the bid is {highest_bidder}, with the bid of ${highest_bid}")