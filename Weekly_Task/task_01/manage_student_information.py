# Collect student details
student_name = "Abhay Yadav"  # String
student_age = 21  # Integer
grades = [85.5, 90.0, 78.5]  # List of floats for grades

# Calculate total and average grades
total_grades = sum(grades)  # Arithmetic operation
average_grade = total_grades / len(grades)  # Calculate average
average_as_integer = int(average_grade)  # Type conversion to integer

# Determine pass or fail status
passing_marks = 40  # Minimum marks required to pass
pass_status = average_grade >= passing_marks  # Logical and comparison operators

# Format output using escape characters
print("Student Report:\n")
print(f"\tName: {student_name}")
print(f"\tAge: {student_age}")
print(f"\tGrades: {grades}")
print(f"\tAverage Grade: {average_grade:.2f}")  # Format float to 2 decimal places
print(f"\tPass Status: {'Pass' if pass_status else 'Fail'}")

# Display sliced part of the name
print(f"\nSliced Name: {student_name[:5]}")  # Extract the first 4 characters