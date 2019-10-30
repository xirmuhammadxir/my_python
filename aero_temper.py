import urllib.request
def url_open(url:str) -> list:
    lst = list()
    try:
        with urllib.request.urlopen(url) as webpage:
            for line in webpage:
                line = line.decode('utf-8')
                line = line.strip()
                lst.append(line)
        return lst
    except Exception as e:
        return e

k = 0
s = 0
maxx = 0
minn = 0
if __name__ == '__main__':
    str1 = url_open("https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/temper.stat")
    for i in range(len(str1)):
        k += 1
        s = s + float(str1[i])
        if float(str1[i]) > maxx:
               maxx = float(str1[i])
        if float(str1[i]) < minn:
               minn = float(str1[i])
s = s / k
print("Максимальное значение среди полученных значений ", maxx)
print("Максимальное значение среди полученных значений ", minn)
print("Максимальное значение среди полученных значений ", s)
