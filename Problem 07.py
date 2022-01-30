Statement : Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I".

def reverse(str1):
    length = len(str1)
    string = ""
    for i in range(length):
        string = string + str1[length - 1]
        length = length - 1
    return string

print(reverse("I am testing"))
