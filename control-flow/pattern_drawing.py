
def draw_pattern(size):
    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after each row
        row += 1

# Prompt user for the pattern size
try:
    size = int(input("Enter the size of the pattern: "))
    if size > 0:
        draw_pattern(size)
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter a positive integer.")

