a = input("Введите число: ")
S = 0
for i in range(len(a)):
    l = int(a[i])
    if l % 2 == 0:
        continue
    l = l**2
    S += l

print("Сумма квадратов нечетных цифр числе = ",S)
