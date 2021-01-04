from art import logo

#Calculator
def add(n1, n2):
  return n1 + n2

def subtraction(n1,n2):
  return n1 - n2

def multiplication(n1,n2):
  return n1 * n2

def division(n1, n2):
  return n1 / n2

calculator = {
  "+": add,
  "-": subtraction,
  "*": multiplication,
  "/": division
}

def calculation():
  print(logo)
  
  num1 = float(input("What is the first number: "))

  for key in calculator:
    print(key)

  quit = False

  while not quit:
    operation_choice = input("Pick an operation from the line above: ")  

    num2 = float(input("What is the second number: "))

    operation = calculator[operation_choice]
    answer = operation(num1,num2)

    print(f"{num1} {operation_choice} {num2} = {answer}")

    if input(f"Type 'y' to do another operation with {answer} or 'n' to quit: ").lower() == "y":
      num1 = answer
    else:
      quit = True  
      calculation()

calculation()