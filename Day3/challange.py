# BMI Calculator

height = float(input("Enter your height in meter: "))
weight = int(input("Enter your weight: "))

bmi = weight * height * height


if bmi < 18.5:
    print("You are underweight")
elif 18.5 <= bmi < 25:
    print("You are at normal weight")
elif 25 <= bmi < 30:
    print("You are overweight")
elif 30 <= bmi < 35:
    print("You are obese")
elif bmi >= 35:
    print("You are clinically obese")
