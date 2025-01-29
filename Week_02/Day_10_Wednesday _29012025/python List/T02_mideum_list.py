# 1️⃣ Sort a list using sort().
marks = [85, 45, 90, 70, 60]
marks.sort()
print("Sorted list:", marks)

# 2️⃣ Sort a list in descending order.
marks.sort(reverse=True)
print("Descending order:", marks)

# 3️⃣ Find the largest and smallest element.
print("Largest element:", max(marks))
print("Smallest element:", min(marks))

# 4️⃣ Count occurrences of an element in a list.
nums = [1, 2, 3, 1, 2, 1, 4]
print("Count of 1:", nums.count(1))

# 5️⃣ Remove duplicates from a list.
unique_nums = list(set(nums))
print("Unique numbers:", unique_nums)

# 6️⃣ Copy a list using slicing and copy().
original = [10, 20, 30]
copy_list = original[:]
print("Copied list:", copy_list)

# 7️⃣ Concatenate two lists.
list_a = [1, 2, 3]
list_b = [4, 5, 6]
concatenated = list_a + list_b
print("Concatenated list:", concatenated)

# 8️⃣ Check if two lists are equal.
list_x = [1, 2, 3]
list_y = [1, 2, 3]
print("Are lists equal?", list_x == list_y)

# 9️⃣ Find the sum of all elements in a list.
print("Sum of list:", sum(marks))

# 🔟 Find the second largest element in a list.
sorted_list = sorted(marks, reverse=True)
print("Second largest element:", sorted_list[1])
