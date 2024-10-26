""" DS-1043 Lab 7

This module contains functions that help visualize
nested lists/dictionaries into mark-down tables.
Additional functionality includes zipper-merge and
Caesar Cryptography.

Completed by Shaun W. by 26 Oct 2024"""

import os
import io
import string
import shutil

# str left bool middle num right


def create_table(header: list[str, ...], data: list):
# create a list of strings containing a formatted table
# for printing or writing to a file

    # initialize final list
    table_list = []
    columns = []

    # max_widths will find the longest data in characters
    # max_widths will also round all floats to 2 decimals along the way
    columns = max_widths(header, data)

    # goes through and ensure individual lists match header length
    for storage in data:

        if isinstance(storage, list):
            if len(storage) == len(header):
                continue
            elif len(storage) != len(header):
                raise ValueError('Length of lists must be equal to length of header')


    # create heading and bar format, add to table_list
    # since all str type, one space on left, rest at end per
    temp_header = []
    for i in range(len(header)):
        spacing = columns[i] - len(header[i])
        temp_header.append(f"| {header[i]} " + " " * spacing)
    table_list.append(temp_header)

    temp_header = []
    for i in range(len(header)):
        temp_header.append("|-" + "-" * columns[i] + "-")
    table_list.append(temp_header)


    # goes through lists/dicts and adds formatted lists into final result
    for storage in data:

        temp_list = []

        # checks if the set in data is a dict
        if isinstance(storage, dict):
            key_list = list(storage.keys())
            value_list = list(storage.values())

            for i in range(len(header)):

                # checks if dict key matches header
                if key_list[i] == header[i]:

                    # each if deals with corresponding value types and their formatting
                    if isinstance(value_list[i], bool):

                        if value_list[i] is False:
                            spacing = columns[i] - 5
                            temp_list.append(f"| {value_list[i]}" + " " * spacing + " ")
                            continue
                        if value_list[i] is True:
                            spacing = columns[i] - 4
                            temp_list.append(f"| {value_list[i]}" + " " * spacing + " ")
                            continue

                    if isinstance(value_list[i], int):
                        copy = str(value_list[i])
                        if len(copy) > 8:
                            spacing = columns[i] - 8
                            temp_list.append("| " + " " * spacing + f"{value_list[i]:.2e} ")
                        else:
                            spacing = columns[i] - len(copy)
                            temp_list.append("| " + " " * spacing + f"{value_list[i]} ")
                        continue

                    if isinstance(value_list[i], float):
                        copy = str(round(value_list[i], 2))
                        if len(copy) > 8:
                            spacing = columns[i] - 8
                            temp_list.append("| " + " " * spacing + f"{value_list[i]:.2e} ")
                        else:
                            spacing = columns[i] - len(copy)
                            temp_list.append("| " + " " * spacing + f"{value_list[i]:.2e} ")
                        continue

                    if isinstance(value_list[i], str):
                        spacing = columns[i] - len(value_list[i])
                        temp_list.append(f"| {value_list[i]} " + " " * spacing)
                        continue

                elif key_list[i] != header[i]:
                    temp_list.append("| " + " " * columns[i] + " ")

            table_list.append(temp_list)

        # checks if set in data is a list
        if isinstance(storage, list):

            # goes through range for num of columns
            for i in range(len(header)):

                # each if deals with corresponding value types and their formatting
                if isinstance(storage[i], bool):

                    if storage[i] is False:
                        spacing = columns[i] - 5
                        temp_list.append(f"| {storage[i]}" + " " * spacing + " ")
                        continue
                    if storage[i] is True:
                        spacing = columns[i] - 4
                        temp_list.append(f"| {storage[i]}" + " " * spacing + " ")
                        continue

                if isinstance(storage[i], int):
                    copy = str(storage[i])
                    if len(copy) > 8:
                        spacing = columns[i] - 8
                        temp_list.append("| " + " " * spacing + f"{storage[i]:.2e} ")
                    else:
                        spacing = columns[i] - len(copy)
                        temp_list.append("| " + " " * spacing + f"{storage[i]} ")
                    continue

                if isinstance(storage[i], float):
                    copy = str(round(storage[i], 2))
                    if len(copy) > 8:
                        spacing = columns[i] - 8
                        temp_list.append("| " + " " * spacing + f"{storage[i]:.2e} ")
                    else:
                        spacing = columns[i] - len(copy)
                        temp_list.append("| " + " " * spacing + f"{storage[i]:.2e} ")
                    continue

                if isinstance(storage[i], str):
                    spacing = columns[i] - len(storage[i])
                    temp_list.append(f"| {storage[i]} " + " " * spacing)
                    continue

            # adds appropriately formatted data to final table
            table_list.append(temp_list)

    # testing without view table below
    #
    # for i in range(len(table_list)):
    #     line_str = ''
    #     for j in table_list[i]:
    #         line_str += j
    #     print(line_str)

    return table_list



def view_table(header, data, max_width=(shutil.get_terminal_size()).columns, file=None):
    # print the table to the console
    # this function should call `create_table`
    # pass the file keyword parameter to the print function
    # this will allow writing to a stream for testing

    # grab formatted table from create_table() function
    viewing = create_table(header, data)
    # grab count of columns
    num_columns = len(header)
    # grab list of column widths
    data_widths = max_widths(header, data)
    table_width = 0
    for item in data_widths:
        # add three due to create_table() formatting
        # from "| " (2) and " " (1) characters per item
        table_width += (3 + item)

    # final table_width will be the character count width of the entire table
    if max_width >= table_width + 1: # "+ 1" to account for adding "|"
        for i in range(len(viewing)):
            viewing[i].append("|")

    else:
        while True:
            if max_width < table_width + 1: # "+ 1" to account for adding "…"
                # remove last item/column from table
                for i in range(len(viewing)):
                    viewing[i].pop(-1)
                # recheck/re-assign width values for next while iteration
                table_width = 0
                # simply check length of header for width
                for j in viewing[0]:
                    table_width += len(j)
            else:
                break
        for i in range(len(viewing)):
            viewing[i].append("…")


    for v in range(len(viewing)):
        line = ''
        for t in viewing[v]:
            line += t
        print(line, file=None)


def max_widths(header, data) -> list:

    widths = []
    widest = None
    copy = ''

    # beginning column max widths grabbed from header lengths
    for word in header:
        widths.append(len(word))

    # goes through data lists/dicts in the range of num of header columns
    for i in range(len(header)):

        widest = None

        # checks each list/dict
        for item in data:

            # checking widths in lists
            if isinstance(item, list):

                # each if deals with finding widths of the data as appropriate
                if isinstance(item[i], bool):
                    if widest is None or widest < 5:
                        widest = 5

                if isinstance(item[i], int):
                    copy = str(item[i])
                    if len(copy) > 8:
                        if widest is None or widest < 8:
                            widest = 8
                    elif widest is None or len(copy) > widest:
                        widest = len(copy)

                if isinstance(item[i], float):
                    item[i] = round(item[i], 2)
                    copy = str(round(item[i], 2))
                    if len(copy) > 8:
                        if widest is None or widest < 8:
                            widest = 8
                    elif widest is None or len(copy) > widest:
                        widest = len(copy)

                if isinstance(item[i], str):
                    if widest is None or len(item[i]) > widest:
                        widest = len(item[i])

                if widest > widths[i]:
                    widths[i] = widest

            # checking widths in dicts
            if isinstance(item, dict):

                # each if deals with finding widths of the data as appropriate
                key_list = list(item.keys())
                value_list = list(item.values())
                if isinstance(value_list[i], bool):
                    if widest is None or widest < 5:
                        widest = 5

                if isinstance(value_list[i], int):
                    copy = str(value_list[i])
                    if len(copy) > 8:
                        if widest is None or widest < 8:
                            widest = 8
                    elif widest is None or len(copy) > widest:
                        widest = len(copy)

                if isinstance(value_list[i], float):
                    value_list[i] = round(value_list[i], 2)
                    copy = str(round(value_list[i], 2))
                    if len(copy) > 8:
                        if widest is None or widest < 8:
                            widest = 8
                    elif widest is None or len(copy) > widest:
                        widest = len(copy)

                if isinstance(value_list[i], str):
                    if widest is None or len(value_list[i]) > widest:
                        widest = len(value_list[i])

                if widest > widths[i]:
                    widths[i] = widest

    return widths




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

    # returns a single new list of the ordered values
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