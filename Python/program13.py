# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 15:51:44 2024

@author: HR bharath Bhat
"""

def print_time(time1, time2):
    # Extract hours, minutes, and seconds from the time objects
    hours1, minutes1, seconds1 = time1['hours'], time1['minutes'], time1['seconds']
    hours2, minutes2, seconds2 = time2['hours'], time2['minutes'], time2['seconds']
    
    # Sum the seconds, and handle overflow to minutes
    total_seconds = seconds1 + seconds2
    extra_minutes, seconds = divmod(total_seconds, 60)
    
    # Sum the minutes, including any overflow from seconds, and handle overflow to hours
    total_minutes = minutes1 + minutes2 + extra_minutes
    extra_hours, minutes = divmod(total_minutes, 60)
    
    # Sum the hours, including any overflow from minutes
    hours = hours1 + hours2 + extra_hours
    
    # Print the result in hour:minute:second format
    print(f"{hours:02}:{minutes:02}:{seconds:02}")


# Example usage:
time1 = {"hours": 3, "minutes": 52, "seconds": 30}
time2 = {"hours": 1, "minutes": 10, "seconds": 40}

print_time(time1, time2)