#Who pays the bill
import random
names_string = input("Please enter the name of all your friends separated by comma.: ")
names = names_string.split(", ")

#print(f"Bill should be paid by {names[random.randint(0, (len(names)-1))]}")
print(f"Bill should be paid by {random.choice(names)}")