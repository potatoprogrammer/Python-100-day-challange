# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

sum = 0
total_items = 0

for item in student_heights:
  sum += item
  total_items += 1  

average = int(sum / total_items)

print(average)