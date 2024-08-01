# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 15:55:26 2024

@author: Hrushik Rajs
"""
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(month, year):
    days_in_months = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_months[month - 1]

def time_until_next_birthday(birth_year, birth_month, birth_day, current_year, current_month, current_day, current_hour, current_minute, current_second):
    # Calculate age
    age = current_year - birth_year
    if (current_month < birth_month) or (current_month == birth_month and current_day < birth_day):
        age -= 1

    # Calculate the year of the next birthday
    if (current_month > birth_month) or (current_month == birth_month and current_day > birth_day):
        next_birthday_year = current_year + 1
    else:
        next_birthday_year = current_year

    # Calculate months until next birthday
    months = birth_month - current_month
    if months < 0:
        months += 12

    # Calculate days until next birthday
    days = birth_day - current_dayA
    if days < 0:
        if current_month == 12:
            days += days_in_month(1, next_birthday_year)
        else:
            days += days_in_month(current_month + 1, current_year)
        months -= 1

    # Calculate hours, minutes, and seconds until next birthday
    hours = 23 - current_hour
    minutes = 59 - current_minute
    seconds = 59 - current_second
    
    return age, {
        "months": months,
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }

# Example usage:
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))
current_year = 2024
current_month = 8
current_day = 1
current_hour = 3
current_minute = 0
current_second = 0

age, time_remaining = time_until_next_birthday(birth_year, birth_month, birth_day, current_year, current_month, current_day, current_hour, current_minute, current_second)
print(f"You are {age} years old.")
print(f"Time until next birthday: {time_remaining['months']} months, {time_remaining['days']} days, {time_remaining['hours']} hours, {time_remaining['minutes']} minutes, {time_remaining['seconds']} seconds.")
