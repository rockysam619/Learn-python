#Tip Calculator

print("** Welcome to the tip calculator **\n")
bill = float(input("What is the total bill amount? : $"))
tip_percent = int(input("What is the percentage you would like to tip? 10, 12 or 15?: "))
people = int(input("How many people will split the bill? : "))

tip = bill*(tip_percent/100)
each_pay = (bill + tip)/people

print(f"Tip amount is: ${round(tip, 2)}")
print(f"Each Person should pay: ${round(each_pay, 2)}")