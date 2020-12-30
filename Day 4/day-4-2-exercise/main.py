# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
names_length = len(names)

random_payer = random.randint(0, names_length - 1)

print(f"{names[random_payer]} is going to buy the meal today!")

#a better way to do

print(f"{random.choice(names)} is going to buy the meal today!")
