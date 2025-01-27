# 1. Number Range Check
# Write a program that asks the user for a number. If the number is between 10 and 50 (inclusive), print "Number is in range." 
# Otherwise, print "Number is out of range."

number = int(input("Enter your Number : "))
if 10 <= number <= 50:
    print("Number is in range.")
else:
    print("Number is out of range.")

#-------------------------------------------------------------------------------------------------------------------------------------

# 2. Multiple Conditions
# Write a program that takes a number as input. If the number is divisible by both 3 and 5, print "FizzBuzz". 
# If divisible only by 3, print "Fizz". If divisible only by 5, print "Buzz". Otherwise, print the number.

div_number = int(input("Enter number : "))
if div_number % 3 == 0 and div_number % 5 == 0:
    print("FizzBuzz.")
elif div_number % 3 == 0:
    print("Fizz.")
elif div_number % 5 == 0:
    print("Buzz.")
else:
    print(div_number)

# -------------------------------------------------------------------------------------------------------------------------------------

# 3. Grade Assignment
# Write a program that takes a score (out of 100) as input and assigns grades:
# 90 and above: "A"
# 80 to 89: "B"
# 70 to 79: "C"
# Below 70: "Fail"

score = int(input("Enter You Score out of 100 : "))
if score >= 90:
    print("You achieved Grade A")
elif 80 <= score <= 89:
    print("You achieved Grade B")
elif 70 <= score <= 79:
    print("You achieved Grade C")
else:
    print("You Failed")

# -------------------------------------------------------------------------------------------------------------------------------------

# 4. Triangle Validity Checker
# Write a program that takes three sides of a triangle as input and checks if the triangle is valid (sum of any two sides is greater than the third).
side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: "))
side3 = float(input("Enter the third side of the triangle: "))
# Check for triangle validity
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")

# -------------------------------------------------------------------------------------------------------------------------------------

# 5. Login System
# Write a program that asks for a username and password. If the correct combination is "admin" and "password123", print "Access granted." Otherwise, print "Access denied."
username = input("Enter your username : ")
password = input("Enter your password : ")
if username == "admin" and password == "password123":
    print("Access granted")
else:
    print("Access denied.")
