#test file for lab 3 functions
#Shaun Worthen DS1043
import time
import lab3 as ds
#DEBUG SWITCH AT END OF CODE#
#DEBUG SWITCH AT END OF CODE#
#DEBUG SWITCH AT END OF CODE#
#DEBUG SWITCH AT END OF CODE#


def test_is_odd():
    assert ds.is_odd(1) is True
    assert ds.is_odd(2) is False
    assert ds.is_odd(3.45) is False
    assert ds.is_odd(4.2) is False
    assert ds.is_odd(-1) is True
    assert ds.is_odd(-2) is False
    assert ds.is_odd(-3.3) is False


def test_is_even():
    assert ds.is_even(1) is False
    assert ds.is_even(2) is True
    assert ds.is_even(3.4) is False
    assert ds.is_even(4.2) is False
    assert ds.is_even(-1) is False
    assert ds.is_even(-2) is True
    assert ds.is_even(-3.3) is False


#RELEVANT UNIX CONVERSIONS BELOW#
# 1 second = 1
# 1 minute = 60
# 1 hour = 3600
# 1 day = 86400

def test_time_elapsed():
    assert (ds.time_elapsed(round(time.time()) - 1)) == (0,0,0,1)
    assert (ds.time_elapsed(round(time.time()) - 64)) == (0,0,1,4)
    assert (ds.time_elapsed(round(time.time()) - 3696)) == (0,1,1,36)
    assert (ds.time_elapsed(round(time.time()) - 91103)) == (1,1,18,23)
    assert (ds.time_elapsed(round(time.time()) - 0)) == (0,0,0,0)


def test_area():
    assert ds.area(0,12) == 0
    assert ds.area(3,0) == 0
    assert ds.area(12,12) == 144
    assert ds.area(2.5,3) == 7.5
    assert ds.area(2,10.2) == 20.4


def test_perimeter():
    assert ds.perimeter(0,0) == 0
    assert ds.perimeter(3,0) == 6
    assert ds.perimeter(12,6) == 36
    assert ds.perimeter(2.5,1.25) == 7.5
    assert ds.perimeter(5,5) == 20


def test_volume():
    assert ds.volume(0,0,0) == 0
    assert ds.volume(3,0,0) == 0
    assert ds.volume(0,6,0) == 0
    assert ds.volume(0,0,9) == 0
    assert ds.volume(3,1,9) == 27
    assert ds.volume(4,2,5) == 40


def test_surface_area():
    assert ds.surface_area(0,0,0) == 0
    assert ds.surface_area(2,4,0) == 16
    assert ds.surface_area(0,5,2) == 20
    assert ds.surface_area(3,4,5) == 94


def test_square_color():
    assert ds.get_square_color(0,0) == "White"
    assert ds.get_square_color(5,0) == "Black"
    assert ds.get_square_color(5,2) == "Black"
    assert ds.get_square_color(5,5) == "White"

#RELEVANT UNIX CONVERSIONS BELOW#
# 1 second = 1
# 1 minute = 60
# 1 hour = 3600
# 1 day = 86400
def test_pretty_time():
    assert ds.prettify_time(0,0,0,0) == ""
    assert ds.prettify_time(3,0,0,0) == "3 days"
    assert ds.prettify_time(3,3,0,0) == "3 days, 3 hours"
    assert ds.prettify_time(1,2,3,4) == "1 day, 2 hours, 3 minutes, 4 seconds"
    assert ds.prettify_time(1,1,1,1) == "1 day, 1 hour, 1 minute, 1 second"


def test_right_justify():
    assert ds.right_justify("test1", 10) == "          " + "test1"
    assert ds.right_justify("test2", 3) == "   " + "test2"
    assert ds.right_justify("test3", 2) == "  " + "test3"


def test_center_justify():
    assert ds.center_justify("test1", 6) == "      " + "test1" + "      "
    assert ds.center_justify("test2", 3) == "   " + "test2" + "   "
    assert ds.center_justify("test3", 2) == "  " + "test3" + "  "


def test_fizz_buzz():
    assert ds.fizz_buzz(1) == "1 "
    assert ds.fizz_buzz(2) == "1 2 "
    assert ds.fizz_buzz(3) == "1 2 Fizz "
    assert ds.fizz_buzz(5) == "1 2 Fizz 4 Buzz "
    assert ds.fizz_buzz(15) == "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz "


def test_ordinal_suffix():
    assert ds.ordinal_suffix(1) == "1st"
    assert ds.ordinal_suffix(2) == "2nd"
    assert ds.ordinal_suffix(3) == "3rd"
    assert ds.ordinal_suffix(4) == "4th"
    assert ds.ordinal_suffix(5) == "5th"
    assert ds.ordinal_suffix(11) == "11th"
    assert ds.ordinal_suffix(12) == "12th"
    assert ds.ordinal_suffix(13) == "13th"
    assert ds.ordinal_suffix(112) == "112th"
    assert ds.ordinal_suffix(2934) == "2934th"
    assert ds.ordinal_suffix(0) == "0th"
    assert ds.ordinal_suffix(12942) == "12942nd"

#debug switch. if on and code run, then the following:
#if no errors/no output code works!! :)
#if error, follow IDE debugging
debug = 1
if debug == 1:
    test_is_odd()
    test_is_even()
    test_time_elapsed()
    test_area()
    test_perimeter()
    test_volume()
    test_surface_area()
    test_square_color()
    test_pretty_time()
    test_right_justify()
    test_center_justify()
    test_fizz_buzz()
    test_ordinal_suffix()