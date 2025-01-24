<h3>1. Write a program to determine the largest of three numbers using comparison operators.</h3>

```
no1 = 156843
no2 = 569836
no3 = 485132

if no1 > no2 and no1 > no3:
    print("no1 is the largest number of three.")
elif no2 > no1 and no2 > no3:
    print("no2 is the largest number of three.")
else:
    print("no3 is the largest number of three.")

```

**Screen short of output📝**
![image](https://github.com/user-attachments/assets/bcf2b58c-4b6a-4a06-a668-470cab848da6)

---

<h3>2. Check if a number is between 50 and 100 using logical operators.</h3>

```
number1 = 84
if number1 > 50 and number1 < 100:
    print(f"{number1} number is between 50 and 100")
else:
    pass
```

**Screen short of output📝**
![image](https://github.com/user-attachments/assets/6c754bab-a379-4e89-a2c2-a05e1a53e49b)

---

<h3>3. Calculate the total cost after applying a 10% discount to a product price.</h3>

```
price = float(input("Enter the product price: "))
discount = price * 0.10
final_price = price - discount

if price < 0:
    print("Invalid price. Please enter a positive value.")
else:
    discount = price * 0.10
    final_price = price - discount
    print(f"Total Price after Discount: {final_price}")
```

**Screen short of output📝**
![image](https://github.com/user-attachments/assets/d3ae78a0-21e9-4861-b9ad-4cad2bd79e97)

---

<h3>4. Write a program to check if a given year is a leap year.</h3>

```
year = 2025
if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
```

**Screen short of output📝**
![image](https://github.com/user-attachments/assets/e95f72d7-447a-4259-91ef-aaf974cdadc1)

---

<h3>5. Using logical operators, check if a number is divisible by both 3 and 5.</h3>

```
no1 = 15
if no1 % 3 == 0 and no1 % 5 == 0:
    print(f"{no1} number is divisible by both 3 and 5")
else:
     pass
```

**Screen short of output📝**
![image](https://github.com/user-attachments/assets/ade0117c-37ff-4feb-a8e9-98e46c725fbc)

---

<h3>6. Write a program to find the average of 5 numbers entered by the user.</h3>

```
no1 = int(input("enter no1:"))
no2 = int(input("enter no2:"))
no3 = int(input("enter no3:"))
no4 = int(input("enter no4:"))
no5 = int(input("enter no5:"))
average = (no1 + no2 + no3 + no4 + no5) / 5
print(average)
```

**Screen short of output📝**
![image](https://github.com/user-attachments/assets/72b49897-954c-4862-9fa0-261a31a9f926)

---

<h3>7. Implement a basic calculator with options for addition, subtraction, multiplication, and division using arithmetic operators.</h3>

```
no1 = 12
no2 = 3
add = no1 + no2
sub = no1 - no2
multi = no1 * no2
div = no1 / no2
print(f"addition of {no1} and {no2} is:", add)
print(f"subtraction of {no1} and {no2} is:", sub)
print(f"multiplication of {no1} and {no2} is:", multi)
print(f"division of {no1} and {no2} is:", div)
```

**Screen short of output📝**
![image](https://github.com/user-attachments/assets/0ec0f5d6-d5be-46c4-af96-d5f2963fab5e)

---

<h3>8. Write a program to determine if a character is a vowel or consonant using logical operators.</h3>

```
if char in 'aeiou':
    print(f"{char} is a vowel.")
elif char.isalpha():  # Check if it is a letter but not a vowel
    print(f"{char} is a consonant.")
else:
    print("Invalid input. Please enter a letter.")
```

**Screen short of output📝**
![image](https://github.com/user-attachments/assets/60462df9-044b-4c6c-ac30-977c72330222)

---

<h3>9. Using comparison operators, check if two strings are the same.</h3>

```
str1 = "python is good programing language"
str2 = "python is good programing language"
if str1 == str2:
    print("both string are same")
else:
    pass
```

**Screen short of output📝**
![image](https://github.com/user-attachments/assets/15aaef0f-40d0-47ed-851a-1ee3efb57790)

---

<h3>10. 10.Write a program to calculate the simple interest using the formula SI = (P * R * T) / 100.</h3>

```
P = 1000
R = 5
T = 2
 
simple_interest = (P * R * T) / 100
print("The Simple Interest (SI) is:", simple_interest)
```

**Screen short of output📝**
![image](https://github.com/user-attachments/assets/0e760224-0636-4111-a963-44e37317c80e)

---
