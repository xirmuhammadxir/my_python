from random import randint
def max_5(a,b, c,l):
    for i in range(len(a)-4):
        b = int(a[i]) + int(a[i+1]) + int(a[i+2]) + int(a[i+3]) + int(a[i+4])
        if b > c:
            c = b
            l = a[i:i+5]
    return l

b = 0
c = 0
l = []
a = [randint(-20,30)for _ in range(20)]
print (a)
print("5 соседних элементов, сумма значений которых максимальна: ",max_5(a,b,c,l))
