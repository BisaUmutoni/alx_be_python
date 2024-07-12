
task = input("Enter the task description: ")

priority = input("Enter the task priority (high, medium, low): ").lower()

time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Function to generate reminder
def generate_reminder(task, priority, time_bound):
    
    reminder = f"Reminder: {task}. Priority: {priority.capitalize()}."

    match priority:
        case "high":
            reminder += " This is a high-priority task."
        case "medium":
            reminder += " This is a medium-priority task."
        case "low":
            reminder += " This is a low-priority task."
        case _:
            reminder += " Priority level is not recognized."

    if time_bound == "yes":
        reminder += " This task requires immediate attention today!"

    return reminder

reminder_message = generate_reminder(task, priority, time_bound)
print(reminder_message)

