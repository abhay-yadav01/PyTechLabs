# 1. Basic Number Comparison....
# Write a program that takes a number as input and prints "Positive" if the number is greater than 0, otherwise prints "Non-positive".
print("Wellcome to number Comparison !!!\n")
x = int(input("Enter your number : "))
if x>0:
    print(x, "is Positive number.")
else:
    print(x, "is Non-Positive number.")

#-------------------------------------------------------------------------------------------------------------------------------------

# 2. Even or Odd....
# Write a program that checks if a number is even or odd. 
print("\nWellcome to even or odd number!!!\n")
number = int(input("Enter your number : "))
if number % 2 == 0:
    print(number, "is Even number.")
else:
    print(number, "is odd number.")

#-------------------------------------------------------------------------------------------------------------------------------------

# 3. Age Check
# Write a program that asks for a user's age. If the user is 18 or older, print "You are eligible to vote." Otherwise, print "You are not eligible to vote."
print("\nWellcome to vote!!!\n")
age = int(input("Enter your Age : "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#-------------------------------------------------------------------------------------------------------------------------------------

# 4. Check for Discount
# Write a program that asks the user for the total shopping bill amount. If the amount is greater than 1000, print "You are eligible for a discount." Otherwise, print "No discount available."
bill_amount = int(input("Enter your total shopping bill amount : "))
if bill_amount >= 1000:
    print("You are eligible for a discount.")
else:
    print("No discount available.")

#-------------------------------------------------------------------------------------------------------------------------------------

# 5. Grade Checker
# Write a program that takes a number as input. If the number is greater than or equal to 50, print "Pass". Otherwise, print "Fail".
marks = int(input("Enter your Marks = "))
if marks >= 50:
    print("Pass")
else:
    print("Fail")