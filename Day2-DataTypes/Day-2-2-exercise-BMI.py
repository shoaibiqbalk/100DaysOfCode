print("*---Body Mass Index (BMI) Calculator---*")

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

BMI = int(weight / (height**2))

print(f"Your BMI is {BMI}")