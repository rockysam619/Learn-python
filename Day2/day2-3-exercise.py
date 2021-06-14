# Calculate your life left in weeks if you live upto 90 years old

age = int(input("Enter your current age: "))

years_left = 90 - age


print(f"You have {years_left*12} months, {years_left*52} weeks and {years_left*365} days left.")