# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 15:47:46 2024

@author: H bharath Bhat
"""
def calculate_day_of_week(year, month, day):
    # Zeller's Congruence algorithm to calculate the day of the week
    if month < 3:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    f = day + 13*(month + 1)//5 + K + K//4 + J//4 + 5*J
    day_of_week = f % 7
    return day_of_week

def get_current_date():
    # Get current date (Replace this with current date input manually)
    year = int(input("Enter the current year: "))
    month = int(input("Enter the current month: "))
    day = int(input("Enter the current day: "))
    return year, month, day

def print_day_of_week(day_of_week):
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    print(f"Today is {days[day_of_week]}.")

# Example usage:
year, month, day = get_current_date()
day_of_week = calculate_day_of_week(year, month, day)
print_day_of_week(day_of_week)
