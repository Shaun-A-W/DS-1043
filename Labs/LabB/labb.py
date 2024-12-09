def bubble_sort(data: list, reverse=False) -> list:
    while True:
        swaps = 0
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swaps += 1
            else: continue
        if swaps == 0:
            break
    return data


def merge_sort(data: list, reverse=False) -> list:
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[0:mid]
    right = data[mid:]

    arr_L = merge_sort(left)
    arr_R = merge_sort(right)

    return merge(arr_L, arr_R)

def merge(first, second, reverse=False) -> list:
    array = []
    x = 0
    y = 0
    while x < len(first) and y < len(second):
        if first[x] <= second[y]:
            array.append(first[x])
            x += 1
            continue
        array.append(second[y])
        y += 1

    while x < len(first):
        array.append(first[x])
        x += 1

    while y < len(second):
        array.append(second[y])
        y += 1

    return array


def bisect_search(sorted_data: list, value) -> int:
    if len(sorted_data) < 2 or value > sorted_data[-1]:
        return -1

    bottom = 0
    top = len(sorted_data) - 1

    while bottom <= top:
        med = (top + bottom) // 2
        if value == sorted_data[med]:
            return med
        elif value > sorted_data[med]:
            bottom = med + 1
        elif value < sorted_data[med]:
            top = med - 1


# d = [random.randint(0,100) for _ in range(9)]
# print("data set: ", d)
# print("merge set: ", merge_sort(d))
#
# d = [random.randint(0,100) for _ in range(11)]
# print("data set: ", d)
# print("bubble set: ", bubble_sort(d))
#
# d = [1,6,9,52,109]
# print(bisect_search(d, 1001))


class Node:

    def __init__(self, value, parent=None):
        self._parent = parent
        self._left = None
        self._right = None
        self._value = value
        self._quantity = 1

    def __repr__(self):
        if self._left is None and self._right is None:
            return f'{self._value}'
        return f'{self._value} ({self._left}, {self._right})'

    def __eq__(self, other):
        return self._value == other

    def __gt__(self, other):
        return self._value > other

    def __lt__(self, other):
        return self._value < other

    def __le__(self, other):
        return self._value <= other

    def __ge__(self, other):
        return self._value >= other

    def insert(self, value):
        if value < self:
            if self._left is None:
                self._left = Node(value, self)
            else:
                self._left.insert(value)
        elif value > self:
            if self._right is None:
                self._right = Node(value, self)
            else:
                self._right.insert(value)
        elif value :
            self._quantity = self._quantity + 1


import random
random.seed()

root = None

for item in {random.randint(0,100) for _ in range(20)}:
    if root is None:
        root = Node(item)
    else:
        root.insert(item)

print(root)