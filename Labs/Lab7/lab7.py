""" DS-1043 Lab 7

This module contains functions that help visualize
nested lists/dictionaries into mark-down tables.
Additional functionality includes zipper-merge and
Caesar Cryptography.

Completed by Shaun W. by 22 Oct 2024"""

import os
import io
import string


def create_table(header, data):
    pass
# create a list of strings containing a formatted table
# for printing or writing to a file



# def view_table(header, data, max_width=(os.get_terminal_size()).columns, file=None):
#     pass
# print the table to the console
# this function should call `create_table`
# pass the file keyword parameter to the print function
# this will allow writing to a stream for testing


def merge_sorted_lists(lists: list[list[int,...],...]) -> list:

    # starting vars
    zipped = []
    element_count = 0

    while True:

        # restarts each var per loop
        smallest = None
        smallest_track = None

        # counts total elements across all lists
        for order in lists:
            element_count += len(order)

        # checks if there are any elements/numbers left
        # if none left, breaks loop
        if element_count < 1:
            break
        else: element_count = 0

        # goes through the enumeration of "lists"
        # which checks the state of entire collection per loop
        for num, order in enumerate(lists):

            # checks to see if current list of numbers is empty or not
            if len(order) != 0:

                current = lists[num][0]

                # for each enumerated list, compares and notes down
                # the smallest number seen & it's corresponding list
                if smallest is None or current < smallest:
                    smallest = current
                    smallest_track = num

        zipped.append(smallest)
        lists[smallest_track] = lists[smallest_track][1:]

    return zipped


def caesar(rotation: int, plaintext: str) -> str:

    # starting vars
    ciphertext = ''
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    # note: 'a' is 97 'z' is 122
    # note: 'A' is 65 'Z' is 90

    # goes through each inputted character in the plaintext
    for char in plaintext:

        # checks if character is part of the uppercase or lowercase alphabet
        # if not, such as a number, adds plaintext version without encrypting
        if char not in lower and char not in upper:
            ciphertext += char
            continue

        # checks to see which alphabet the character is in.
        # according to that, uses the rotation and the chr / ord functions
        # to assign the corresponding letter to its ciphertext counterpart
        if char in lower:
            tag = ord(char)
            new_tag = (tag - ord('a') + rotation) % 26 + ord('a')
            ciphertext += chr(new_tag)
        if char in upper:
            tag = ord(char)
            new_tag = (tag - ord('A') + rotation) % 26 + ord('A')
            ciphertext += chr(new_tag)

    # returns the encrypted plaintext according to the shift value
    return ciphertext