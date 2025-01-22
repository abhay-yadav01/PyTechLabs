<h3>1. Write a program to demonstrate the use of global keyword.</h3>

```
str = "good"
def myfunction():
    global str
    str = "grate"
myfunction()
print(f"python is {str} programing lanuage.")
```

**Screen short of output📝**
![image](https://github.com/user-attachments/assets/60209570-c645-45ad-a7b7-2e290a06e3b3)

---

<h3>2. Create a function that uses a local variable and a global variable with the same name.</h3>

```
var = "yadav"
def myfun():
    # global var
    var = "abhay"
    print(f"my first name is {var}")
myfun()
print(f"my last name is {var}")
```

**Screen short of output📝**
![image](https://github.com/user-attachments/assets/a2589c7f-fc90-488d-b5c7-5a269f9630b0)

---

<h3>3. Write a program to compare two variables using is operator.</h3>

```
no1 = 5546
no2 = 5546
if no1 == no2:
    print(f"{no1} and {no2} both are same")
else:
    pass
```

**Screen short of output📝**
![image](https://github.com/user-attachments/assets/6fb3e844-053a-4df6-a07f-7b7281418082)

---
