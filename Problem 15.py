Statement : Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

def find_longest_word(list_var):
    value = []
    for i in list_var:
        value.append(len(i))
    value.sort()
    return value[-1]

word_list = ['Java', 'Python', 'PHP', 'C']
print(find_longest_word(word_list))
