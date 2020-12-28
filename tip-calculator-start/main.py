#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator.")

bill_total = input("What was the total bill? $")
bill_total_float = float(bill_total)

tip_percentage = input("What percentage tip woul you like to give? 10, 12, or 15? ")
tip_percentage_int = int(tip_percentage)

total_people = input("How many people to split the bill? ")
total_people_int = int(total_people)

total_with_tip = bill_total_float * (1 + (tip_percentage_int / 100))
total_with_tip = round(total_with_tip, 2)

price_divided = total_with_tip / total_people_int

price_divided = round(price_divided, 2)

print(f"Each person should pay: ${price_divided}")