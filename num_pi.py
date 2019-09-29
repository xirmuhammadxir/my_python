import math
l = math.pi
a=int(input("Выберите цифру 1 или 0\n"))
if a == 1:
    q=f'{l:.5f}'
    print(q)
elif a == 0:
    q=f'{l:.10f}'
    print(q)
else:
    print("Введите правильную цифру!!!")
