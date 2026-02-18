# ps1b.py
# Assignment 1 - Part B: Saving with a Raise
# Author: Hemanth Pramidhala
# Collaborators: None
# Inputs
annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
# Constants
portion_down_payment = 0.25
current_savings = 0
r = 0.04
months = 0
monthly_salary = annual_salary / 12
down_payment = total_cost * portion_down_payment
while current_savings < down_payment:
    # Investment return
    current_savings += current_savings * (r / 12)
    # Savings from salary
    current_savings += monthly_salary * portion_saved
    months += 1
    # Apply raise every 6 months
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12
print("Number of months:", months)
