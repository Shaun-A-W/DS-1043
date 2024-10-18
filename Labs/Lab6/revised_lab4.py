"""Revised Lab 4 DS-1043

This module implements rudimentary functions for basic statistics
and probability.

Completed by Shaun W. by 2024-10-18 (YYYY-MM-DD) for DS-1043"""

#imports etc
import random
Number = int | float
Sequence = list | tuple


def lab_min(numbers: Sequence) -> Number :
    if len(numbers) < 1:
        raise ValueError("Given sequence is empty")
    sort_min = sorted(numbers)
    return sort_min[0]


def lab_max(numbers: Sequence) -> Number :
    if len(numbers) < 1:
        raise ValueError("Given sequence is empty")
    sort_max = sorted(numbers, reverse=True)
    return sort_max[0]


def lab_sum(numbers: Sequence) -> Number :
    sum_of_numbers = 0
    i = 0
    if len(numbers) < 1:
        raise ValueError("Given sequence is empty")
    for element in numbers:
        sum_of_numbers = sum_of_numbers + numbers[i]
        i += 1
    return sum_of_numbers


def lab_avg(numbers: Sequence) -> Number :
    if len(numbers) < 1:
        raise ValueError("Given sequence is empty")
    avg_sum = lab_sum(numbers)
    avg_of_numbers = avg_sum / len(numbers)
    return avg_of_numbers


def lab_median(numbers: Sequence) -> Number :
    if len(numbers) < 1:
        raise ValueError("Given sequence is empty")
    numbers = sorted(numbers)
    if len(numbers) % 2 != 0:
        odd_length = round((len(numbers))) / 2
        return numbers[int(odd_length)]
    elif len(numbers) % 2 == 0:
        even_length = (len(numbers) - 1) / 2
        return (numbers[int(even_length)] + numbers[int(even_length + 1)]) / 2


def lab_mode(numbers: Sequence) -> list | None :
#beginning, check if viable input & define vars
    if len(numbers) < 1:
        raise ValueError("Given sequence is empty")
    mode_list = {}
    mode_value = None
    modes = []
    if len(numbers) == 1:
        modes = [numbers[0]]
        return modes
#construct the dictionary w/ keys & values
    for item in numbers:
        if item not in mode_list:
            mode_list[item] = 1
        else:
            mode_list[item] = mode_list[item] + 1
#check for highest repetition value(s), if value < 2, return none
    for key in mode_list.keys():
        if mode_value is None:
            mode_value = mode_list[key]
        elif mode_value < mode_list[key]:
            mode_value = mode_list[key]
    if mode_value == 1 and len(numbers) > 1:
        return None
#find keys associated with the highest repetition value
    for key, value in mode_list.items():
        if value == mode_value:
            modes = modes + [key]
    return modes


def roll_dice(dice: int, faces: int) -> tuple[tuple[int,int],...] :
    if dice < 1 or faces < 1:
        raise ValueError("Must be at least one dice and at least one face each")
    list_dice = []
    for i in range(1, dice+1):
        list_dice = list_dice + [(i, random.randint(1, faces))]
    return tuple(list_dice)


#random module important
random.seed()