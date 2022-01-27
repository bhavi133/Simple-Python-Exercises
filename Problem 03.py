Statement : Define a function that computes the length of a given list or string. (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise).

def custom_length(input):
    if (not isinstance(input, str)) and (not isinstance(input, list)):
        raise TypeError("Parameter should be list or string type")
    ctr = 0
    for i in input:
        ctr += 1
    return ctr

print(custom_length("abc"))
