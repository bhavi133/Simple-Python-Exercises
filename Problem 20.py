Statement : Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} and use it to translate your Christmas cards from English into Swedish. That is, write a function translate()that takes a list of English words and returns a list of Swedish words dic = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "år"}

def translate(list_eng):
    dic = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "år"}
    list_dic = [dic[i] for i in list_eng]
    return list_dic

list_eng = ['merry', 'christmas']
print(translate(list_eng))
