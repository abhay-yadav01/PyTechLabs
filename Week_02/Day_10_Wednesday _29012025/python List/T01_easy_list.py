# 1️⃣ Create and print a list.
first_list = ["abhay", "yadav"]
print(first_list)

# 2️⃣ Access list elements using positive and negative indexing.
list01 = ["apple", "banana", "orange", "kiwi"]
# print first 2 elements using +ve index
print("first two elements:", list01[:2])
# print last 2 elements using -ve index
print("last two elements:", list01[-2:])

# 3️⃣ Modify an element in the list.
companies = ["BhavinTechnoLabs", "IBM", "Google", "Oasis", "Ubrain", "Sunflower"]
companies[4] = "TCS"
print("after modification:", companies)

# 4️⃣ Append and extend a list.
# for append method
fruits = ["Apple", "Banana"]
fruits.append("Cherry")
print("After append:", fruits)
# for extend method
vegetables = ["Carrot", "Potato"]
fruits.extend(vegetables)
print("After extend:", fruits)

# 5️⃣ Insert an element at a specific index.
numbers = [10, 20, 30, 50]
numbers.insert(3, 40)
print("After insertion:", numbers)

# 6️⃣ Remove an element using pop().
students = ["Ravi", "Amit", "Pooja", "Neha"]
students.pop(2)
print("After pop:", students)

# 7️⃣ Use del to delete a specific element.
colors = ["Red", "Blue", "Green", "Yellow"]
del colors[1]
print("After deletion:", colors)

# 8️⃣ Check if an element exists in the list.
if "Apple" in fruits:
    print("Apple is in the list")

# 9️⃣ Find the length of the list.
print("List length:", len(fruits))

# 🔟 Reverse the list using reverse().
numbers.reverse()
print("After reverse:", numbers)
