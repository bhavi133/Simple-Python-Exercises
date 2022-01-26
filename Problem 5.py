Statement : Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun") should return the string "tothohisos isos fofunon".

import string

def translate(text):
    if (not isinstance(text, str)):
        raise TypeError("Parameter should be string.")

    letters = string.ascii_letters
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    consonant = [i for i in letters if i not in vowels]
    result = ""
    for i in text:
        if i in consonant:
            result = result + i + "o" + i
        else:
            result = result + i
    return result

print(translate("this is fun"))
