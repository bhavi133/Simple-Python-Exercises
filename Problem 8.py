Statement : Define a function is_palindrome()that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True

def is_palindrome(str1):
    length = len(str1)
    string = ""
    for i in range(length):
        string = string + str1[length-1]
        length = length - 1
    if str1 == string:
        return True
    else:
        return False

print(is_palindrome("radar"))
print(is_palindrome("abcde"))
