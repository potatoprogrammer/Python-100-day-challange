first_array = [1,3,4,5,0,2,28,77,432,2984,248]
second_array = []
third_array = [3]
fourth_array = [4,4,1]

def find_second(my_array):
  bigest = None
  second = None
  for item in my_array:
    if bigest == None:
      bigest = item
    elif item > bigest:  
      bigest = item

  for item in my_array:
    if second == None and item < bigest:
      second = item
    elif second != None:
      if item > second and item < bigest:
        second = item
  return second

print(find_second(first_array))       
print(find_second(second_array))   
print(find_second(third_array))
print(find_second(fourth_array))