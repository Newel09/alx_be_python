"""
Objective: Create a simplified Python script that uses conditional statements, Match Case, and loops 
to remind the user about a single, priority task for the day based on time sensitivity.

Task Description:

Develop a script named daily_reminder.py. This script will ask the user for a single task, 
its priority level, and if it is time-sensitive. The program will then provide a customized 
reminder for that task, demonstrating control flow and loops without relying on data structures 
to store multiple tasks.
"""

# Prompt for a single task
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Enter the priority level (high, medium, low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Process the task based on priority using Match Case
match priority:
    case "high":
        reminder = f"URGENT: {task} is a HIGH priority task"
    case "medium":
        reminder = f"IMPORTANT: {task} is a MEDIUM priority task"
    case "low":
        reminder = f"NOTE: {task} is a LOW priority task"
    case _:
        reminder = f"REMINDER: {task} - Priority not recognized, treat as medium priority"

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += "."

# Print the customized reminder
print("\n" + "="*60)
print(reminder)
print("="*60)

# Loop to ask if the user wants another reminder
while True:
    another = input("\nWould you like to set another reminder? (yes or no): ").lower()
    if another == "yes":
        # Reset and get new task information
        task = input("Enter your task: ")
        priority = input("Enter the priority level (high, medium, low): ").lower()
        time_bound = input("Is the task time-bound? (yes or no): ").lower()
        
        # Process the new task based on priority
        match priority:
            case "high":
                reminder = f"URGENT: {task} is a HIGH priority task"
            case "medium":
                reminder = f"IMPORTANT: {task} is a MEDIUM priority task"
            case "low":
                reminder = f"NOTE: {task} is a LOW priority task"
            case _:
                reminder = f"REMINDER: {task} - Priority not recognized, treat as medium priority"
        
        # Modify the reminder if the task is time-bound
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += "."
        
        # Print the customized reminder
        print("\n" + "="*60)
        print(reminder)
        print("="*60)
    else:
        print("Thank you for using the Daily Reminder. Have a productive day!")
        break