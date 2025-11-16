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
Task = str(input("Enter your task: "))

Priority = str(input("Priority (high, medium, low): ").lower())

Time_Bound = str(input("Is the task time-bound (yes or no)? ").lower())

match (Priority, Time_Bound):
    case ("high", "yes"):
        print(f"Reminder: '{Task}' is a {Priority} priority task that requires immediate attention today!")
    case ("high", "no"):
        print(f"Reminder: '{Task}' is a {Priority} priority task but can be done tomorrow.")
    case ("medium", "yes"):
        print(f"Reminder: '{Task}' is a {Priority} priority task but needs time attention.")
    case ("medium", "no"):
        print(f"Reminder: '{Task}' is a {Priority} priority task and does not need immediate attention.")
    case ("low", "yes"):
        print(f"Reminder: '{Task}' is a {Priority} priority task. Consider working on it soon.")
    case ("low", "no"):
        print(f"Reminder: '{Task}' is a {Priority} priority task. Consider completing it when you have free time.")
    case _:
         print("Invalid!")
