def avg_word_length(file):
    file = open(file, 'r', encoding = 'utf-8')
    words = []
    for line in file:
        for word in line.strip("!.:;,?-/$%()").split(" "):
            words.append(len(word))
    avg_words = sum(words)/len(words)
    return avg_words
print(avg_word_length('Ebook.txt'))