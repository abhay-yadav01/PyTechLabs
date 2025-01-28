# 1. Print Numbers from 1 to 10
# Write a program using a for loop to print numbers from 1 to 10.

for i in range(1,11):
    print(i)

#-----------------------------------------------------------------------------------------------------------------------------------

# 2. Print Each Character in a String
# Write a program that takes a string as input and uses a for loop to print each character in the string.

string = str(input("Enter Your string : "))
for character in string:
    print(character)

#-----------------------------------------------------------------------------------------------------------------------------------

# 3. Sum of Numbers in a List
# Write a program to calculate the sum of all numbers in a list using a for loop.
# Example: For the list [1, 2, 3, 4, 5], the output should be 15.
numbers = [1, 2, 3, 4, 5]
total_sum = 0
for number in numbers:
    total_sum += number
    print("The sum of the numbers in the list is:", total_sum)

#-----------------------------------------------------------------------------------------------------------------------------------

# 4. Print Even Numbers in a Range
# Write a program that uses a for loop to print all even numbers between 1 and 20.

for i in range(2,21,2):
    print("Even number :",i)
# or
# Use a for loop to iterate through the range
print("Even numbers between 1 and 20 are:")
for number in range(1, 21):
    if number % 2 == 0:  # Check if the number is even
        print(number)

#-----------------------------------------------------------------------------------------------------------------------------------

# 5. Print a Pattern
# *
# **
# ***
# ****
# *****
'''for i in range(1,6):
    print("*" * i)'''
# Or second way
for i in range(1,6):
    for j in range(1,6):
        if j<=i:
            print("*", end=" ")
        else:
            print("", end="")
    print()