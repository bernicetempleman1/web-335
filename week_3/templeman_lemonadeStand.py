"""
Author: Bernice Templeman
Date: 06/08/2024
File Name: templeman_lemonadeStand.py
Description: This program uses the print function to output the cost and profit calculations.
"""

""" @method: calculate_cost.
    @description: Method to calculate the total cost.
    @params: lemons_cost, sugar_cost
    @returns: Floating point value.
"""
def calculate_cost(lemons_cost, sugar_cost):
    total_cost = lemons_cost + sugar_cost  # Calculating the total cost
    return total_cost  # Returning the total cost

""" @method: calculate_profit.
    @description: Method to calculate the profit.
    @params: lemons_cost, sugar_cost, selling_price
    @returns: Floating point value.
"""
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    # In the body of the function, return the profit from selling the lemonade.
    profit = selling_price - calculate_cost(lemons_cost, sugar_cost)
    return profit

# variables to test each function.
lemons_cost = 5.00
sugar_cost = 3.00
selling_price = 10.00

# Call each function passing in the variables you created in step 4
total_cost = calculate_cost(lemons_cost, sugar_cost)
profit = calculate_profit(lemons_cost, sugar_cost, selling_price)

# Use a variable to build a string for the results: format: (cost of lemons) + (cost of sugar) = (total cost).
results = '${0:.2f} (cost of lemons) + ${1:.2f} (cost of sugar) = ${2:.2f} (total cost).'.format(
    lemons_cost, sugar_cost, total_cost)

# print the results to the console using an output variable and string concatenation.
print('{0} The profit is ${1:.2f}'.format(results, profit))
