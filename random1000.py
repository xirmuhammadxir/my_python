from random import randint
kolO = 0
a = [randint(-2000,2000)for _ in range(1000)]
x = [i for i in range(min(a),max(a)) if (i in a) and (i < 0)]
for i in x:
    kolO += 1
print(kolO)
