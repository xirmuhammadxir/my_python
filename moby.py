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

if __name__ == '__main__':
    str_new = []
    strr = url_open("https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/moby.txt")
    strr = str(strr)
    strr.split(" ")
    for i in range (len(strr)):
        with open("moby_clean.txt", 'a') as output_file:
            output_file.write(strr)
        a = strr[i].lower()
        str_new.append(a)
    out = "".join(i for i in strr if i not in ('!','.',':',',','?'))
    str_new = "".join(str_new)
    print (str_new)
    print(out)
    
