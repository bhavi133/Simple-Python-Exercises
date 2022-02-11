Statement : Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
Write it in three different ways:
1) Using a for-loop
2) Using the higher order function map()
3) Using list comprehensions

def map_word_with_length_using_for_loop(word_list):
    dic = dict()
    for i in word_list:
        dic[i] = len(i)
    return dic

def map_word_with_length_using_map(word_list):
    word_len_list = list(map(lambda x: len(x), word_list))
    return dict(zip(word_list, word_len_list))

def map_word_with_length_using_list_comprehension(word_list):
    word_len_list = [len(i) for i in word_list]
    return dict(zip(word_list, word_len_list))

word_list = ['Java', 'PHP', 'HTML', 'C', 'Python']
print(map_word_with_length_using_for_loop(word_list))
print(map_word_with_length_using_map(word_list))
print(map_word_with_length_using_list_comprehension(word_list))
