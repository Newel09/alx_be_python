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
"""
task = str(input("Enter your task: "))

task_priority = str(input("Priority (high, medium, low): ").lower())

time = str(input("Is the task time-bound (yes or no)? ").lower())

match (task_priority, time):
    case ("high", "yes"):
        print(f"Reminder: '{task}' is a {task_priority} priority task that requires immediate attention today!")
    case ("high", "no"):
        print(f"Reminder: '{task}' is a {task_priority} priority task but can be done tomorrow.")
    case ("medium", "yes"):
        print(f"Reminder: '{task}' is a {task_priority} priority task but needs time attention.")
    case ("medium", "no"):
        print(f"Reminder: '{task}' is a {task_priority} priority task and does not need immediate attention.")
    case ("low", "yes"):
        print(f"Reminder: '{task}' is a {task_priority} priority task. Consider working on it soon.")
    case ("low", "no"):
        print(f"Reminder: '{task}' is a {task_priority} priority task. Consider completing it when you have free time.")
    case _:
         print("Invalid!")
