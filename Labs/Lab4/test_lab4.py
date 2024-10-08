"""Lab 4 DS-1043 TESTING SCRIPTS
This file is used for testing lab 4 functionality
Completed by Shaun W. by 2024-09-24 (YYYY-MM-DD) for DS-1043"""

import lab4 as ds
import random

def test_lab_min():
    assert ds.lab_min([]) is None
    assert ds.lab_min([1,2,3]) == 1
    assert ds.lab_min([6,2,8]) == 2
    assert ds.lab_min([6,8,8,565,4,9]) == 4


def test_lab_max():
    assert ds.lab_max([]) is None
    assert ds.lab_max([1,2,3]) == 3
    assert ds.lab_max([6,2,8]) == 8
    assert ds.lab_max([6,8,8,565,4,9]) == 565
    assert ds.lab_max([6,8,6,8,6,8,6,8]) == 8


def test_lab_sum():
    assert ds.lab_sum([1,2,3]) == 6
    assert ds.lab_sum([6,2,8]) == 16
    assert ds.lab_sum([6,5,1,9]) == 21
    assert ds.lab_sum([]) is None
    assert ds.lab_sum([0]) == 0


def test_lab_avg():
    assert ds.lab_avg([1,2,3]) == 2
    assert ds.lab_avg([6,2]) == 4
    assert ds.lab_avg([6,5,1,9]) == 5.25
    assert ds.lab_avg([]) is None
    assert ds.lab_avg([0]) == 0


def test_lab_median():
    assert ds.lab_median([1,2,3]) == 2
    assert ds.lab_median([6,2,8]) == 6
    assert ds.lab_median([6,8,8,565,4,9]) == 8
    assert ds.lab_median([1,3,7,10]) == 5
    assert ds.lab_median([]) is None
    assert ds.lab_median([0]) == 0


def test_lab_mode():
    assert ds.lab_mode([1, 2, 3, 4, 5]) is None
    assert ds.lab_mode([3,3,3,4,4,6,7]) == [3]
    assert ds.lab_mode([]) is None
    assert ds.lab_mode([2,2,2,5,5,5,7,1,3,4]) == [2,5]
    assert ds.lab_mode([98]) == [98]


def test_roll_dice():
    assert ds.roll_dice(1,1) == ((1,1),)
    assert ds.roll_dice(2,1) == ((1,1), (2,1))
    assert ds.roll_dice(3,1) == ((1,1), (2,1), (3,1))
    assert ds.roll_dice(0,2) is None
    assert ds.roll_dice(3,0) is None
    assert ds.roll_dice(0,0) is None


#random module important
random.seed()

debug = 1 #on = 1, off = other
if debug == 1:
    test_lab_min()
    test_lab_max()
    test_lab_sum()
    test_lab_avg()
    test_lab_median()
    test_lab_mode()
    test_roll_dice()