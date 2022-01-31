Statement : Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metllic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored

def check_palindrome(string):
    string = string.lower()
    string = "".join([i for i in string if i.isalnum()])
    return string == string[::-1]

test_string1 = "Was it a rat I saw?"
print (check_palindrome(test_string1))

test_string2 = "Step on no pets"
print (check_palindrome(test_string2))

test_string3 = "Not palindrome at all!"
print (check_palindrome(test_string3))
