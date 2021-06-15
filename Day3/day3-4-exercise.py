#Pizza order 
size = input("Please enter the Pizza size: S, M or L?\n")
bill = 0
if size == 'S':
    bill = 15
    print("Small pizza is $15")
elif size == 'M':
    bill = 20
    print("Medium pizza is $20")
else:
    bill = 25
    print("Large pizza is $25")

extra_p = input("Do you need extra pepperoni? Y or N? : ")

if size == 'S' and  extra_p == 'Y':
    bill+=2

if size == 'M' or size == 'L' and extra_p == 'Y':
    bill+=3

extra_c = input("Do you need extra cheese? Y or N? : ")

if extra_c == 'Y':
    bill+=1

print(f"Your total bill is ${bill}")