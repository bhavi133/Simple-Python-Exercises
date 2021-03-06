Statement : Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

def check_vowel(single_char):
    vowels = list('aeiou')
    if ((not isinstance(single_char, str)) and (len(single_char) != 1)):
        raise TypeError("Parameter should be a single character.")
    single_char = single_char.lower()
    return single_char in vowels

print(check_vowel("U"))
