# Highest score using for loops
score_list = (input("Enter scores separated by space:\n")).split(" ")
high = 0

for score in score_list:
   if int(score) > high:
       high = int(score)

print(f"Highest score of the class is {high}")
