def chet(a):
    if a%2 == 0:
        return ("Введённое вами число чёткое")
    else:
        return ("Оно не чётное((")

a = int(input("Введите число, которое хотите проверить на чёткость и чётность: "))
print(chet(a))
