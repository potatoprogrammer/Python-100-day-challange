def is_polindrome(word):
  word_array = []
  inverted = ""
  for item in range(0,len(word)):
    word_array.append(word[item])   
  
  counter = len(word) - 1

  for item in range(0, len(word)):
    inverted += word_array[counter]
    counter -= 1

  if word == inverted:
    return print("This word is a polindrome.")
  else:
    return print("This word is not a polindrome.")
    
  #simpler, but open to failure
  # if word[0] == word[-1] and word[1] == word[-2]:
  #   return print("This word is a polindrome.")
  # else:
  #   return print("This word is not a polindrome.")

word = input("Type a word to check if it is a polindrome: ").lower()

is_polindrome(word)