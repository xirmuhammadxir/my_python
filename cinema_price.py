data=input("Вы пойдёте на фильм сегодня или завтра? \n")
if data=="сегодня":
    d=1
else:
    d=0.95
kol=int(input("Сколько вас человек?\n"))
if kol>=20:
    k=0.8
else:
    k=1
film=input("Выберите фильм и время на который хотите пойти \n")
if film=="Пятница на 12" or film=="Чемпионы на 10":
    print("Цена билета",250*k*d)
elif film=="Пятница на 16" or film=="Чемпионы на 13" or film=="Пернатая банда на 10" or film=="Чемпионы на 16":
    print("Цена билета",350*k*d)
elif "Пятница на 20" or film=="Пернатая банда на 14" or film=="Пернатая банда на 18":
     print("Цена билета",450*k*d)
else:
    print("Введите, пожалуйста, в правильном формате: *Название* На *время*")
