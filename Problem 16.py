Statement : Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.

def filter_long_words(list_var, n):
    value = []
    for i in list_var:
        if len(i) > n:
            value.append(i)
    return value

word_list = ['Java', 'Python', 'PHP', 'C', 'JavaScript']
print(filter_long_words(word_list, 5))
