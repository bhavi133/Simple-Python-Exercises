Statement: Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it. Represent the frequency listing as a python dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab")

def char_freq(string):
    dic = {}
    for i in string:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    dic = dict(sorted(dic.items()))
    return dic

print(char_freq("abbabcbdbabdbdbabababcbcbab"))
