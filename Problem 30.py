Statement : Represent a small bilingual lexicon as a python dictionary in the following fashion: {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "år"}and use it to translate your Christmas cards from English into Swedish. 
Use the higher order function map() to write a function translate() that takes a list of English words and returns a list of Swedish words.

def translate(word_list):
    dic = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "år"}
    return list(map(lambda x: dic[x] if x in dic else False, word_list))

word_list = ['merry', 'and', 'new', 'sad']
print(translate(word_list))
