# DS-1043 Lab 3 Assignment
# Shaun W

"""
This is a library/module which contains functions for:

    Lab 2 functions in addition to FizzBuzz and Ordinal suffixes

Constructed by Shaun W, due on 2024-09-17 (YYYY/MM/DD).
"""

# necessary module supplements below
import math
import time
import datetime


# Even/Odd booleans
def is_odd(eo_number: int) -> bool:
    """is_odd checks if a number is odd.
    if even return false, if odd return true
    only for integers"""
    if type(eo_number) != int:
        return False
    else:
        return eo_number % 2 != 0


def is_even(eo_number: int) -> bool:
    """is_even checks if a number is even.
    if even return true, if odd return false.
    only for integers"""
    if type(eo_number) != int:
        return False
    else:
        return eo_number % 2 == 0


# Time elapsed
def time_elapsed(timestamp: int) -> tuple[int, int, int, int]:  #[day, hour, min, sec]
    """uses UNIX input timestamp and time record at execution
    to determine the elapsed time since timestamp and execution time"""
    begin = round(time.time())
    elapsed = int(round(begin - timestamp))
    a = elapsed // 86400
    elapsed = elapsed % 86400
    b = elapsed // 3600
    elapsed = elapsed % 3600
    c = elapsed // 60
    elapsed = elapsed % 60
    d = elapsed
    return a, b, c, d


# Shape parameters
def area(length: float, width: float) -> float:
    """given a length and width value,
    returns the area of the rectangle."""
    return length * width


def perimeter(length: float, width: float) -> float:
    """given a length and width value,
    returns the perimeter of the rectangle"""
    return 2 * (length + width)


def volume(length: float, width: float, height: float) -> float:
    """given a length and width value,
    returns the volume of the rectangular prism"""
    return length * width * height


def surface_area(length: float, width: float, height: float) -> float:
    """given a length and width value,
    returns the surface area of the rectangular prism"""
    return (2 * length * width) + (2 * length * height) + (2 * width * height)


# Board color
def get_square_color(column: int, row: int) -> str:
    """starting at bottom left (0,0) column and row @ white,
    uses even/odd booleans to determine checkerboard color"""
    if is_odd(eo_number=column) and is_odd(eo_number=row):
        return "White"
    if is_even(eo_number=column) and is_even(eo_number=row):
        return "White"
    if is_odd(eo_number=column) and is_even(eo_number=row):
        return "Black"
    if is_even(eo_number=column) and is_odd(eo_number=row):
        return "Black"


# Pretty printed time & related

def prettify_time(days: int, hours: int, minutes: int, seconds: int) -> str:
    """uses user inputted 4 value tuple and adds
    respective days, hours, minutes, and seconds labels"""
    timings = [days,hours,minutes,seconds]
    time_names = ['day', 'hour', 'minute', 'second']
    timetagged = []
    x = -1
    for element in timings:
        if element < 1:
            x += 1
            pass
        if element == 1:
            x += 1
            timetagged.append(f"{element} {time_names[x]}")
        if element > 1:
            x += 1
            timetagged.append(f"{element} {time_names[x]}s")
    return ', '.join(timetagged)

# Text justification
def right_justify(content: str, width: int) -> str:
    """adds right justification with
    spaces (according to width) before string"""
    return " " * width + content


def center_justify(content: str, width: int) -> str:
    """adds center justification with
    spaces (according to width to each side) before/after string"""
    return " " * width + content + " " * width


def fizz_buzz(up_to: int) -> str:
    """Generates, for each number from 1 to input,
    fizz for div by 3, buzz for div by 5, and fizzbuzz for both.
    if neither, print number. only for integers"""
    if up_to < 1:
        return "Num must be > 1"
    else:
        pass
    fizz_out = ""
    for i in range(1, up_to + 1):
        if i % 3 == 0 and i % 5 == 0:
            fizz_out = fizz_out + "FizzBuzz "
        elif i % 3 == 0 and i % 5 != 0:
            fizz_out = fizz_out + "Fizz "
        elif i % 3 != 0 and i % 5 == 0:
            fizz_out = fizz_out + "Buzz "
        elif i % 3 != 0 and i % 5 != 0:
            fizz_out = fizz_out + str(i) + " "
    return fizz_out


def ordinal_suffix(number: int) -> str:
    """generates ordinal suffix for number input
    and returns string"""
    if type(number) != int:
        return "Not an integer"
    else:
        pass
    #exception case for ending in 11 - 19
    if number % 100 == 11 or number % 100 == 12 or number % 100 == 13 or number % 100 == 14 or number % 100 == 15 or number % 100 == 16 or number % 100 == 17 or number % 100 == 18 or number % 100 == 19:
        return str(number) + "th"
    #end exception
    elif number % 10 == 0:  #for ending in 0
        return str(number) + "th"
    elif number % 10 == 1:  #ending 1
        return str(number) + "st"
    elif number % 10 == 2:  #ending 2
        return str(number) + "nd"
    elif number % 10 == 3:  #ending 3
        return str(number) + "rd"
    elif 3 < number % 10 <= 9:  #ending 4 through 9
        return str(number) + "th"
