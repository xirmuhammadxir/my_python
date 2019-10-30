def histogram(s):
    word_count = {}
    for word in s:
        word_count.setdefault(word, 0)  # word_count[key] = 0, если такого key не было ранее
        word_count[word] += 1 # word_count[word] = word_count[word] + 1        
    return word_count

with open('moby_clean.txt','r') as file:
    for line in file:
        for word in line.split():
            word = line.strip()
if __name__ == "__main__":
    print (histogram(word.split()))
    print (max(histogram(word.split())))
    print (min(histogram(word.split())))
