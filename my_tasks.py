zad = []
cont = ("")
while cont != "выход"   :
    z = input("Введите задачу: ")
    time = input("До какого времени нужно выполнить данную задачу? ")
    zad.append([z,time])
    print(zad)
    cont = input("Для продолжения нажмите Enter, для окончаня записи напишите: выход: ")
