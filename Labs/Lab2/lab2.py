# DS-1043 Lab 2 Assignment
# Shaun Worthen

"""
This is a library/module which contains functions for:

    Odd / Even number boolean,
    Elapsed time,
    Shape parameters in a given space (area, perimeter, volume, surface area),
    Chess Board color coordinates,
    Elapsed time in 'pretty print',
    Text justification,

Constructed by Shaun Worthen on 2024-09-03 (YYYY/MM/DD).
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
    if eo_number % 2 == 0:
        print(False)
        return False
    elif eo_number % 2 != 0:
        print(True)
        return True

def is_even(eo_number: int) -> bool:
    """is_even checks if a number is even.
    if even return true, if odd return false.
    only for integers"""
    if eo_number % 2 == 0:
        print(True)
        return True
    elif eo_number % 2 != 0:
        print(False)
        return False

# Time elapsed
def time_elapsed(timestamp: int) -> tuple[int, int, int, int]:#[day, hour, min,sec]   -> time_el()[1]
    """uses UNIX input timestamp and time record at execution
    to determine the elapsed time since timestamp and execution time"""
    begin = time.time()
    elapsed = int(round(begin - timestamp))
    a = elapsed // 86400
    elapsed = elapsed % 86400
    b = elapsed // 3600
    elapsed = elapsed % 3600
    c = elapsed // 60
    elapsed = elapsed % 60
    d = elapsed
    print(a, b, c, d)
    return[a, b, c, d]

# Shape parameters
def area(length: float, width: float) -> float:
    """given a length and width value,
    returns the area of the rectangle."""
    print(length * width)
    return (length * width)

def perimeter(length: float, width: float) -> float:
    """given a length and width value,
    returns the perimeter of the rectangle"""
    print(2*(length + width))
    return (2*(length + width))

def volume(length: float, width: float, height: float) -> float:
    """given a length and width value,
    returns the volume of the rectangular prism"""
    print(length * width * height)
    return (length * width * height)

def surface_area(length: float, width: float, height: float) -> float:
    """given a length and width value,
    returns the surface area of the rectangular prism"""
    print((2 * length * width) + (2 * length * height) + (2 * width * height))
    return ((2 * length * width) + (2 * length * height) + (2 * width * height))

# Board color
def get_square_color(column: int, row: int) -> str:
    """starting at bottom left (0,0) column and row @ white,
    uses even/odd booleans to determine checkerboard color"""
    if is_odd(eo_number=column) and is_odd(eo_number=row):
        print("White")
    if is_even(eo_number=column) and is_even(eo_number=row):
        print("White")
    if is_odd(eo_number=column) and is_even(eo_number=row):
        print("Black")
    if is_even(eo_number=column) and is_odd(eo_number=row):
        print("Black")

# Pretty printed time
def prettify_time(timestamp) -> str:
    """uses user inputted UNIX 'timestamp' with time_elapsed() function
    and adds respective days, hours, minutes, and seconds labels"""
    begin = time.time()
    elapsed = int(round(begin - timestamp))
    a = elapsed // 86400
    elapsed = elapsed % 86400
    b = elapsed // 3600
    elapsed = elapsed % 3600
    c = elapsed // 60
    elapsed = elapsed % 60
    d = elapsed
    print(a, "days", b, "hours", c, "minutes", d, "seconds")
    #ignore the following return "{} days {} hours {} minutes {} seconds".format(days, hours, minutes, seconds);#    print(time_elapsed(timestamp)[0] "days", time_elapsed(timestamp)[1] "hours", time_elapsed(timestamp)[2] "minutes", time_elapsed(timestamp)[3] "seconds")

# Text justification
def right_justify(content: str, width: int) -> str:
    """adds right justification with
    spaces (according to width) before string"""
    print(" "*width, content)

def center_justify(content: str, width: int) -> str:
    """adds center justification with
    spaces (according to width to each side) before/after string"""
    print(" "*width, content, " "*width)