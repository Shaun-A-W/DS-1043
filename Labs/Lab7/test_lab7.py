""" This file is for testing the functions
created for DS-1043 Lab 7

Completed by Shaun W. alongside Lab 7."""

import lab7 as ds

# table testing start
data_l = [['abcd',1234567,100,True],[33,False,'alphabeta',231311223.333334]]
data_d = [{'a': 233, 'two': 'c', 'd': False, 'four': 12222222222222}, {'one': 12.399, 'two': '3', 'three': True, 'four': False}]
header = ['a','two','three','four',]

data_wide = [[1,2,3,4,5,6,7,8,9,0,11,12,13],[1,2,3,4,5,6,7,8,9,0,11,12,13]]
header_wide = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen']

ds.view_table(header, data_l, file=None)
print("\n")
ds.view_table(header, data_d, file=None)
print("\n")
ds.view_table(header_wide, data_wide, file=None)
assert ds.max_widths(['alpha','beta','charlie','delta'], [[False, 'one', 'chocolate', 123456789],[1,2,3,4]]) == [5,4,9,8]
# table testing end

# zipper tests
assert ds.merge_sorted_lists([[1,2,3,45],[1,7,7],[65]]) == [1,1,2,3,7,7,45,65]
assert ds.merge_sorted_lists([[4,6,8],[1,6,9],[2,3]]) == [1,2,3,4,6,6,8,9]
assert ds.merge_sorted_lists([[1,5],[2,4]]) == [1,2,4,5]

# caesar tests
assert ds.caesar(1,'abc') == 'bcd'
assert ds.caesar(2, 'shaun') == 'ujcwp'
assert ds.caesar(30, 'python') == 'tcxlsr'