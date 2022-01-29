Statement : Write a function max_in_list() that takes a list of numbers and returns the largest one

def max_in_list(list_var):
    max = list_var[0]
    for i in list_var:
        if i > max:
            max = i
    return max

list_var = [3, 7, 98, 34, 12, 14]
print(max_in_list(list_var))
