# Calculating the BMI 2.0

height = float(input("Enter your height in metres\n"))
weight = float(input("Enter your weight in kgs\n"))

# BMI formula
bmi = round(weight/(height**2))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight")
elif bmi<25:
    print(f"Your BMI is {bmi}, you have a normal weight")
elif bmi<30:
    print(f"Your BMI is {bmi}, you are slightly overweight")
elif bmi<35:
    print(f"Your BMI is {bmi}, you are obese")
else:
    print(f"Your BMI is {bmi}, you are clinically obese")
