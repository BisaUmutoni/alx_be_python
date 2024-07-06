from datetime import datetime, timedelta

# Function to display current date and time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

# Function to calculate future date based on input days
def calculate_future_date():
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now() 
        convert_date_time = timedelta(days=number_of_days)
        future_date = current_date + convert_date_time
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date after {number_of_days} days: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter a valid number of days.")

# Main function to run the script
def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()

