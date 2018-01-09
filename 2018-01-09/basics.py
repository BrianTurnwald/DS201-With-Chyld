# 1 - lists
# order is important, mutable (can change)
odds = [5, 7, 9]
sum(odds)
s = 0
for x in odds:
    s += x

total = 0
for i, num in enumerate(odds):
#enumerate(odd) creates a tuple with (index,value)
#ie for odds: (0,5) (1,7) (2,9)
    total = total + (i*num)

squares = [n**2 for n in odds]
sumsquares = sum([n**2 for n in odds])
squaresdivby5 = [n**2 for n in range(31) if n%5==0]

def square(x):
    return x**2

list(map(square, odds))


reduce(lambda total, n: total + n, odds,10)
reduce(lambda total, n: total * n, odds,1)

# 2 - sets
# no order, iterable, unique, mutable (can change)

s1
{3, 4, 5, 6}

s2
{3, 4, 8, 9}

s1 & s2
{3, 4}

s1 | s2
{3, 4, 5, 6, 8, 9}

s1 ^ s2
{5, 6, 8, 9}


d = {}
for n in range(5):
    d[n] = n**2

#get all keys
d.keys()

#get all values
d.values()

#Get value for a key of 4
d[4]

#have to loop to get keys for a particular value
## :(

#If no key of 5 will error    
d[5]

#Can use get so no error
d.get(5)

#Even better, set default 0 to return a 0
d.get(5,0)

for k, v in d.items():
    print('key',k,'value:',v)
    
key 0 value: 0
key 1 value: 1
key 2 value: 4
key 3 value: 9
key 4 value: 16

{n:n**0.5 for n in range(100) if n%10==0}

#Same thing with List comprehension (list of tuples)
[(n,n**0.50) for n in range(100) if n%10==0]

