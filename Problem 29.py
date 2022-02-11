Statement : Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n

def filter_long_words(lst, n):
    return list(filter(lambda x : len(x) > n, lst))
    # return [i for i in lst if len(i) > n]

lst = ['abc','abcd','abcde','abcdef']
print(filter_long_words(lst, 4))
