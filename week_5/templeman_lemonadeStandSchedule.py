"""
Author: Bernice Templeman
Date: 06/08/2024
File Name: templeman_lemonadeStandSchedule.py
Description: Python program that manages a weekly schedule for a lemonade stand. You will create lists to represent different tasks and use
loops and conditionals to process these lists.
"""

# Defining a list of at least 5 tasks related to running a lemonade stand.
tasks = ["Buy lemons", "Make lemonade", "Sell lemonade", "Count earnings",
         "Clean up"]  # normal level comment explaining this line of code

def display_tasks():
  # Use a for loop to iterate over the list of tasks and print them to the console window.
  for task in tasks:
    print(task)

# Defining a list of days (Sunday through Saturday).
days = ["Sunday", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday", "Saturday"]

# For loop to list days
def display_days():
  for day in days:  # Use a for loop to iterate over the list of days
    print(day)
  print()

# find the task for the day and print it
def find_task(day):
  if day == "Saturday" or day == "Sunday":
    task = "This is a day off and you should rest."
  else:
    index = days.index(day) - 1
    task = tasks[index]
  print('{0}: {1}'.format(day, task))

# Use a for loop to iterate over the list of days and find the task
def list_tasks_by_day():
  for day in days:
    find_task(day)

""" Call the methods and output the results. """
# print tasks to the console window
print("-- LIST OF TASKS --")
display_tasks()

print()

#  use the print function to output the tasks and days of the week: (display a message indicating the day of the week and the corresponding task from the tasks list.)
print("-- TASKS for EACH DAY --")
list_tasks_by_day()
