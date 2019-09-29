import random
a = ["самовар", "весна", "лето"]
w = random.choice(a)
lst_w = list(w)
l = random.choice(lst_w)
i = lst_w.index(l)
lst_w[i] = "?"
w_new = ''.join(lst_w)
print ("Угадайте пропущенную букву в слове ",w_new,":")
u = input()
if u == l:
    print ("Победа!\nСлово:", w)
else:
    print ("Увы! Попробуйте в другой раз.\nСлово:", w)
