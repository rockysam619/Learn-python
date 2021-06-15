#Find a leap year
year = int(input("Please enter a year: "))

if year%4 == 0:
    if (year%100 == 0 and year%400 != 0):
        print("Not a leap year")
    else:
        print("Its a leap year")
else:
    print("Not a leap year")
