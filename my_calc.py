def kal(a,b,c,d):
    try:
        a = int(input("Введите первое число: \n"))
        b = int(input("Введите второе число: \n"))
        c = input("Введите опертатор: ")
        if c == "/":
            d = a/b
        elif c == "+":
            d = a+b
        elif c == "-":
            d = a-b
        elif c == "*":
            d = a*b
        else:
            print("Вы ввели неверный оператор!!!")
        print (d)
    except ZeroDivisionError:
        print("Ошибка деления на ноль!!!")
    except ValueError:
        print("Ошибка преобразования типа!!!")
a = 0
b = 0
c = ""
d = 0
kal(a, b, c, d)
