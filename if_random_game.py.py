import random
x = random.randint(1,4)
a = int(input("Введите число от 1 до 4\n"))
if a==x:
    print("Поздравляю! Вы угадали")
elif 1<a<x or x<a<4:
    print("Упс... Повторите ещё раз((")
else:
    print("Введите число от 1 до 4!!!!")
if 1<a<x:
    print ("Введённое вами число меньше загаданного")
elif x<a<4:
    print ("Введённое вами число больше загаданного")