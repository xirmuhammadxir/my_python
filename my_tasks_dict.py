from pprint import pprint
def add(x,y,z):
    x.append(input("Сформулируйте задачу: "))
    y.append(input("Добавьте категорию к задаче: "))
    z.append(input("Добавьте время к задаче: "))

def vivod(x,y,z):
    for i in range(len(x)):
        print("Задача: ", x[i])
        print("Категория: ", y[i])
        print("Дата: ", z[i])
x = []
y = []
z = []
while 0 == 0:
    print('Простой todo:\n1. Добавить задачу.\n2. Вывести список задач.\n3. Выход.')
    k = int(input("Введите число: "))
    if k == 3:
        break
    dct = {1: add, 2: vivod}
    dct[k](x,y,z)


    
