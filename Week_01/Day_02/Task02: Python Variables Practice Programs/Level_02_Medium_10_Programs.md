<h3>1. Write a program to assign values to variables and swap them without using a third variable.</h3>

```
no1 = 22
no2 = 56
print(no2, no1)
```

---

<h3>2. Create variables to store your name, age, and city. Print them in a sentence.</h3>

```
name = "abhay yadav"
age = 23
city = "jamnagar"
print("my name is", name, "and i am", age, "years old and my city name is", city)
```

---

<h3>3. Write a program to demonstrate the use of multiple assignments (x, y, z = 1, 2, 3).</h3>

```
name, age, city = "abhay", 23, "jamnagr"
print(name, age, city)
```

---

<h3>4. Declare a variable with a float value and convert it to an integer.</h3>

```
pi = 3.14
no1 = int(pi)
print(f"you enter {pi}, convart in integer value is {no1}")
```
---

<h3>5. Write a program to check if two variables share the same memory location using id().</h3>

```
x = 10
y = 10
print(id(x), id(y))
```

---

<h3>6. Write a program to assign a global variable and access it inside a function.</h3>

```
str = "good"
def myfunc():
    print("python is", str, "programing language.")
myfunc()
```
---

<h3>7. Write a program to demonstrate variable reassignment with different data types.</h3>

```
#Refrance form : ChetGPT
x = 10
print("Value of x:", x, "| Type of x:", type(x))
x = "Python"
print("Value of x:", x, "| Type of x:", type(x))
x = 3.14
print("Value of x:", x, "| Type of x:", type(x))
```
---

<h3>8. Create a variable to store a large integer and print its value.</h3>

```
large_number = 123456789012345678901234567890123456789012345678901234567890
print("The large number is:", large_number)
```
---

<h3>9. Write a program to demonstrate dynamic typing by changing the type of a variable.</h3>

```
#Refrance form : ChetGPT
x = 10
print("Value of x:", x, "| Type of x:", type(x))
x = "Python"
print("Value of x:", x, "| Type of x:", type(x))
x = [1,2,3,4,5]
print("Value of x:", x, "| Type of x:", type(x))
x = (1,2,3,4,5)
print("Value of x:", x, "| Type of x:", type(x))
x = {1,2,3,4,5}
print("Value of x:", x, "| Type of x:", type(x))
```
---

<h3>10. Use f-strings to format a sentence with variables.</h3>

```
name = "abhay"
age = 23
language = "python"
sentence = f"my name is {name}, i am {age} years old, i love {language}"
print(sentence)
```
