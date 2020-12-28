# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lower = name1.lower()
name2_lower = name2.lower()

counter1 = 0

counter1 += name1_lower.count("t") + name2_lower.count("t")

counter1 += name1_lower.count("r") + name2_lower.count("r")

counter1 += name1_lower.count("u") + name2_lower.count("u")

counter1 += name1_lower.count("e") + name2_lower.count("e")

counter2 = 0

counter2 += name1_lower.count("l") + name2_lower.count("l")

counter2 += name1_lower.count("o") + name2_lower.count("o")

counter2 += name1_lower.count("v") + name2_lower.count("v")

counter2 += name1_lower.count("e") + name2_lower.count("e")

score = str(counter1) + str(counter2)

score = int(score)

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")  