# ps1a.py
# Assignment 1 - Part A: House Hunting
# Author: Hemanth Pramidhala
# Collaborators: None
# Inputs
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
# Constants
portion_down_payment = 0.25
current_savings = 0
r = 0.04
months = 0
# Monthly salary
monthly_salary = annual_salary / 12
# Down payment needed
down_payment = total_cost * portion_down_payment
# Loop until savings reach down payment
while current_savings < down_payment:
    # Investment return
    current_savings += current_savings * (r / 12)
    # Monthly saving
    current_savings += monthly_salary * portion_saved
    months += 1
# Output
print("Number of months:", months)
