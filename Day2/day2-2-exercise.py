# Calculating the BMI

height = float(input("Enter your height in metres\n"))
weight = float(input("Enter your weight in kgs\n"))

# BMI formula
bmi = weight/(height**2)
print("Your BMI is " + str(int(bmi)))
