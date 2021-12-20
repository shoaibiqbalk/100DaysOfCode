### Challange 1 - Even Or Odd
# number = int(input("Which number do you want to check?"))

## Remember that single "=" is assignment.
## Double "==" is checkinging for equality.
# if number % 2 == 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")
  


### Challange 2 - Leap Year
## This produces a type error when you run it.
## That should be hint to check this line below
## to make sure it is a int and not a string.
# year = int(input("Which year do you want to check?"))

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")


## Challange 3 - FizzBuzz
# for number in range(1, 101):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)