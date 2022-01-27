Statement : Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.

def max_of_three(num1, num2, num3):
    if ((not isinstance(num1, int)) and (not isinstance(num1, float))) or ((not isinstance(num2, int)) and (not isinstance(num2, float))) or ((not isinstance(num3, int)) and (not isinstance(num3, float))):
        raise TypeError("All three parameters should be integer or float.")
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3 and num2 > num1:
        return num2
    else:
        return num3

print(max_of_three(36, -366, 900))
