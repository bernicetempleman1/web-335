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
  # Using a for loop to iterate over the list
  # Use a for loop to iterate over the list of tasks and print them to the console window.
  for task in tasks:
    print(task)

# Defining a list of days (Sunday through Saturday).
days = ["Sunday", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday", "Saturday"]

def display_days():
  for day in days:  # Use a for loop to iterate over the list of days
    print(day)
  print()


def find_task(day):
  # Use a for loop to iterate over the list of days
  if day == "Saturday" or day == "Sunday":
    task = "This is a day off and you should rest."
  elif day == "Monday":
    task = "Buy lemons."
  elif day == "Tuesday":
    task = "Make lemonade"
  elif day == "Wednesday":
    task = "Sell lemonade"
  elif day == "Thursday":
    task = "Count earnings"
  elif day == "Friday":
    task = "Clean up"
  else: print()
  print('{0}: {1}'.format(day, task))


""" Call the methods and output the results. """
print("-- LIST OF TASKS --")
display_days()

print()

print("-- LIST OF TASKS --")
display_tasks()

print()

print("-- TASK for the DAY --")
find_task("Sunday")
