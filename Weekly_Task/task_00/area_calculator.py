# Logic_01: create Separate Logic for Each Shape
# 1. for Circle: Area = 3.14 x (rxr)
# 2. for Rectangle: Area= length x width
# 3. for Triangle: Area= 0.5 × base × height

# using while loop for asking for user again and again
while True:
    print("Choose a shape to calculate the area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Exit")
    # stor the user value in choice variables
    choice = int(input("\nEnter your choice (1 to 4 only): "))
    # hear i am using nested if-else for check and finde the difratn shape of area
# for circle
    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        if radius > 0:
            area = 3.14 * radius**2
            print(f"The area of the circle is: {area:.2f}")
        else:
            print("Radius must be positive.")
# for rectangle
    elif choice == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        if length > 0 and width > 0:
            area = length * width
            print(f"The area of the rectangle is: {area:.2f}")
        else:
            print("Length and width must be positive.")
# for triangle
    elif choice == 3:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        if base > 0 and height > 0:
            area = 0.5 * base * height
            print(f"The area of the triangle is: {area:.2f}")
        else:
            print("Base and height must be positive.")
# for exit form the program
    elif choice == 4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
