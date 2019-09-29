s = "У лукоморья 123 дуб зеленый 456"
a = s.index("я")
b = s.count("у")
c = s.isalpha()
q = int(len(s))
print ("Задание №1: ",a+1)
print ("Задание №2: ",b)
if c == False:
    c = s.upper()
    print ("Задание №3: ",c)
if q > 4:
    q = s.lower()
    print("Задание №4: ",q)
p = "O" + s[1:]
print("Задание №5: ",p)
