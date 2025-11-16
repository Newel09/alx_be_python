"""
Instructions:

Prompt for a Single Task:

Ask the user to input a task description and save it into a task variable
Prompt for the task’s priority (high, medium, low) and save it into a priority variable
In a time_bound variable, Ask if the task is time-bound (yes or no)
"""
"""
Process the Task Based on Priority and Time Sensitivity:

Use a Match Case statement to react differently based on the task’s priority.
Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.
"""

"""
Reminder: 'Finish project report' is a high priority task that requires immediate attention today!
Task
Time Bound
Priority
"""
# Prompt for a Single Task
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use Match Case statement to react based on priority
match priority:
    case "high":
        reminder = f"'{task}' is a HIGH priority task"
    case "medium":
        reminder = f"'{task}' is a MEDIUM priority task"
    case "low":
        reminder = f"'{task}' is a LOW priority task"
    case _:
        reminder = f"'{task}' - Priority not recognized"

# Use an if statement to modify the reminder based on time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += "."

# Print the customized reminder
print("\nReminder: " + reminder)
