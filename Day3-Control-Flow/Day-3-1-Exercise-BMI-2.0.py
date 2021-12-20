print("*---Body Mass Index (BMI) Calculator---*")

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

BMI = int(weight / (height**2))

if BMI > 35:
    print(f"Your BMI is {BMI}, you are clinically obese")
elif BMI > 30:
    print(f"Your BMI is {BMI}, you are obese")
elif BMI > 25:
    print(f"Your BMI is {BMI}, you are slightly overweight")
elif BMI > 18.5:
    print(f"Your BMI is {BMI}, you have a normal weight")
else:
    print(f"Your BMI is {BMI}, you are under weigand")
