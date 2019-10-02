s = 0
while True:
    a = input("Введите число: ")
    if a == "Стоп":
        break
    elif a.isdigit():  
        a = int(a)
        s = s + a
    else:
        print("Повторите ввод числа")
print("Сумма введённых чисел: ",s)
