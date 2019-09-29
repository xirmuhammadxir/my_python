import math
a = []
lst = [2, 4, 9, 16, 25]
for i in range (len(lst)):
    a.append(math.sqrt(lst[i]))
print(a)
b = [math.sqrt(i) for i in lst]
print(b)
def f(x):
    return (math.sqrt(x))

c = list(map(f,lst))
print(c)
