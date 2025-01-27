# 1. Nested Conditions with Marks
# Write a program that asks for the user's total marks out of 500 and calculates the percentage. 
# Then:
# If percentage > 90, print "Grade: A+".
# If percentage is between 75 and 90, print "Grade: A".
# If percentage is between 50 and 74, print "Grade: B".
# Else, print "Grade: Fail".

total_marks = float(input("Enter your total marks out of 500 : "))
percentage = (total_marks / 500) * 100 
if percentage > 90:
    print("Grade: A+")
elif 75 <=  percentage <= 90:
    print("Grade: A")
elif 50 <=  percentage < 74:
    print("Grade: B")
else:
    print("Grade: Fail")

#-----------------------------------------------------------------------------------------------------------------------------------

# 2. Check Leap Year
# Write a program that asks the user for a year and checks:

# If the year is divisible by 400, it's a leap year.
# If divisible by 100 but not by 400, it's not a leap year.
# If divisible by 4 but not by 100, it's a leap year.
# Otherwise, it's not a leap year.

year = int(input("enter year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is leap year.")
else:
    print(f"{year} is not leap year.")
#-----------------------------------------------------------------------------------------------------------------------------------

# 3. ATM Withdrawal Logic
# Write a program for an ATM withdrawal system where:
# If the amount to withdraw is less than or equal to the account balance, print "Transaction successful. Remaining balance: {balance}".
# Otherwise, print "Insufficient balance."

# # Input: Ask user for account balance and withdrawal amount
account_balance = float(input("Enter your account balance: "))
withdraw_amount = float(input("Enter the amount to withdraw: "))
# Check if withdrawal is possible
if withdraw_amount <= account_balance:
    # Update account balance
    account_balance -= withdraw_amount
    print(f"Transaction successful. \nRemaining balance: {account_balance:.2f}")
else:
    print("Insufficient balance.")


#-----------------------------------------------------------------------------------------------------------------------------------

# 4. Find Largest Among Three Numbers
# Write a program that takes three numbers as input and prints the largest of the three.

input_no1 = float(input("Enter your First  number: "))
input_no2 = float(input("Enter your Second number: "))
input_no3 = float(input("Enter your Therad number: "))
if input_no1 > input_no2:
    print(input_no1, "is the largest number.")
elif input_no2 > input_no3:
    print(input_no2, "is the largest number.")
else:
    print(input_no3, "is the largest number.")
    
#-----------------------------------------------------------------------------------------------------------------------------------

# 5. Check Quadrant of a Point
# Write a program that asks the user for the coordinates (x, y) of a point and determines which quadrant the point lies in (1st, 2nd, 3rd, or 4th) or if it lies on an axis.

# Input: Ask user for coordinates
x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))
# 0 = zero & 1 = non-zero
# Logic01 : 
# 1. (x,y) = (0,0) : Origin, 
# 2. (x,y) = (1,0) : OriginOn x-axis, 
# 3. (x,y) = (0,1) : OriginOn y-axis,
# Logic02 : 
# 1st_quadrant (+,+), 
# 2nd_quadrant (-,+), 
# 3rd_quadrant (-,-), 
# 4th_quadrant (+,-), 
if x == 0 and y == 0:
    print("the point is at the Origin.")
elif y == 0:
    print("the point is at the Origin x-axis.")
elif x == 0:
    print("the point is at the Origin y-axis.")
elif x > 0 and y > 0:
    print("The point lies in the 1st Quadrant.")
elif x < 0 and y > 0:
    print("The point lies in the 2nd Quadrant.")
elif x < 0 and y < 0:
    print("The point lies in the 3rd Quadrant.")
elif x > 0 and y < 0:
    print("The point lies in the 4rt Quadrant.")





