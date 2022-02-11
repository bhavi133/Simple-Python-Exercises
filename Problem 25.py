Statement : In English, the present participle is formed by adding the suffix-ing to the infinite form: go -> going. A simple set of heuristic rules can be given as follows:
a. If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
b. If the verb ends in ie, change ie to y and add ing
c. For words consisting of consonant-vowel-consonant, double the final letter before adding ing
d. By default just add ing
Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form returns its present participle form. Test your function with words such as lie, see, move and hug. However, you must not expect such simple rules to work for all cases

import string

def make_ing_form((str1):
    str1 = str1.lower()
    letter = list(string.ascii_lowercase)
    vowel = ['a', 'e', 'i', 'o', 'u']
    consonant = [i for i in letter if i not in vowel]
    exception = ['be', 'see', 'flee', 'knee', 'lie']
    if str1.endswith('e'):
        if str1 in exception:
            return str1 + 'ing'
        else:
            str1 = str1[:-1]
            return str1 + 'ing'

    elif str1.endswith('ie'):
        str1 = str1[:-2]
        return str1 + 'ying'

    elif str1[-1] in consonant and str1[-2] in vowel and str1[-3] in consonant:
        str1 = str1 + str1[-1]
        return str1 + 'ing'

    else:
        return str1 + 'ing'

verb = ['lie', 'see', 'move', 'hug', 'study']
for item in verb:
    print(make_ing_form(item))
