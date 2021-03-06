Statement : A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not

def check_pangram(string):
    string = string.lower()
    char_set = set(string)
    letter_list = [i for i in char_set if i.isalpha()]
    return len(letter_list) == 26

string1 = "The quick brown fox jumps over the lazy dog."
print(check_pangram(string1))

string2 = "This line has not all 26 characters. Okay?"
print(check_pangram(string2))
