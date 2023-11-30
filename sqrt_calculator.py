# Get user input
number = float(input("Enter a number: "))

# Calculate and print the square root
if number >= 0:
    result = number ** 0.5
    print(f"The square root of {number} is: {result}")
else:
    print("Error: Cannot calculate square root of a negative number")
