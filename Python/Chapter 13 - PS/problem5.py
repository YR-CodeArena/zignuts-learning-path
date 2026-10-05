from functools import reduce

lst = [1, 20, 34, 56, 86]
def find_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
    
s = reduce(find_max, lst)
print(s)