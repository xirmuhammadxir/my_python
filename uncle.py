s = "Мой дядя самых честных правил, \
Когда не в шутку занемог, \
Он уважать себя заставил \
И лучше выдумать не мог"
s = s.split(" ")
for i in range(len(s)):
    if s[i].startswith("м"):
        l = s[i]
        s = " ".join(s)
        s = s.replace(l,"")
print(s)
