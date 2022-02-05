Statement : Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers and returns the largest one. Then ask yourself: why define and call a new function, when I can just as well call the reduce() function directly

from functools import reduce

def max_in_list(lst):
    return reduce(lambda x, y : x if (x > y) else y, lst)

lst = [5, 7, 2, 4, 11, 56, 32, 45, 9]
print(max_in_list(lst))
