Statement : Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.

def sum(list1):
    total = 0
    for i in list1:
        total += i
    return total

def multiply(list1):
    total = 1
    for i in list1:
        total *= i
    return total

print(sum([1, 2, 3, 4]))
print(multiply([1, 2, 3, 4]))
