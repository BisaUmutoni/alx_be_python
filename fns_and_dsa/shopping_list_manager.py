#empty list
shopping_list = []

# Function to add an item to the shopping list
def add_item():
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} added to the shopping list.")

# Function to remove an item from the shopping list
def remove_item():
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")

# Function to view the current shopping list
def view_list():
    if shopping_list:
        print("Shopping List:")
        for item in shopping_list:
            print(item)
    else:
        print("Shopping List is empty.")

# Main loop to display the menu and process user input
def main():
    while True:
        print("\nShopping List Manager")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. View the list")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            view_list()
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()

