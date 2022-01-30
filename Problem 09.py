Statement : Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise.(Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator).

def is_member(item, list1):
    length = len(list1)
    for i in range(length):
        if item == list1[i]:
            return True
    return False

list1 = [1, 4, 6, 9, 34]
print(is_member(9, list1))
print(is_member(11, list1))
