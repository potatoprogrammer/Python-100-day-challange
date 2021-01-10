num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

def larger_than(num1, num2): 

  if len(num1) > len(num2):
    if num1[0] > num2[0]:
      print("first number is bigger")
      return True
  elif len(num2) > len(num1):
    if num2[0] > num1[0]:
      print("Second number is bigger") 
      return False 
  elif len(num1) == len(num2):
    for i in range(len(num1)):
      if num1[i] > num2[i]:
        print("first number is bigger")
        return True
      elif num2[i] > num1[i]:
        print("second number is bigger")
        return False
    else:
      print("The numbers are the same")    
      return False

print(larger_than(num1,num2))
