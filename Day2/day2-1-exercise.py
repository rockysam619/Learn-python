# Given a 2 digit number, return the sum of both the digits.

a = input("Please enter a two digit number\n")
b = int(a)
c = int(b/10) + (b%10)

print("Sum of both digits of your 2 digit number is " + str(c))