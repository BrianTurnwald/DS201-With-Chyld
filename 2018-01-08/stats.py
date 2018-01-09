"""
Module/file docstring
Run:
    python -m doctest -v first.py
"""


def add(num1,num2):
    return num1 + num2

def cubevol(length,width,height):
    return length * width * height

def mean(numbers): #works
    sm = 0
    for x in numbers:
        sm += x
    #print(sm)
    #print(len(numbers))
    return sm / len(numbers)

def mean2(numbers): #better
    return sum(numbers) / len(numbers)

def median(numbers): #works
    #number.sort() will change the original variable
    x = sorted(numbers)
    if len(x) %2 == 0:
        mid = int(len(x) / 2)-1
        return (x[mid] + x[mid+1]) / 2
    else:
        mid =  int(len(x)/2)
        return x[mid]

def median2(numbers): #better
    """Computes the median of a list of numbers.
    arguments: list of numbers
    return: the median (int for odd len list, float for even len list)

    >>> median([2,1,6])
    2
    >>> median([3,7])
    5.0
    """
    #number.sort() will change the original variable
    x = sorted(numbers)
    mid = len(x)//2
    if len(x) %2 == 0:
        return sum(x[mid-1:mid+1]) / 2
    else:
        return x[mid]


def mode(numbers):
    """Find the most common value in the list
    arguments: list of numbers
    return: the mode

    >>> mode([9,9,8,8,7,6])
    8
    """
    #defaultdict
    from collections import defaultdict
    d = defaultdict(int)
    for k in numbers:
        d[k] += 1
    for x in d:
        if d[x] > 1:
            p = 'Not Unique, Not Bimodal'
            max_mode = sorted(d, key=lambda key: d[key])[-1]
            max_next = sorted(d, key=lambda key: d[key])[-2]
            if max_mode == max_next:
                p='Bimodal'
                return min(max_mode,max_next)
            else:
                return max(d, key=lambda key: d[key])
        else:
            p = 'Unique'
            return min(d)

    #return max(d, key=lambda key: d[key])
    #or sorted(d, key-lambda key: d[key], reverse=True)[0]
    #or sorted(d, key-lambda key: d[key])[-1]


def mode2(numbers):
    """Find the most common value in the list
    arguments: list of numbers
    return: the mode

    >>> mode([9,9,8,8,7,6])
    8
    """
    #defaultdict
    from collections import defaultdict
    d = defaultdict(int)
    for k in numbers:
        d[k] += 1
    return max(d, key=lambda key: d[key])
