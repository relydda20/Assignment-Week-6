def hapax(file):
    word_list = []
    file = open(file,'r',encoding = 'utf-8')
    words = file.read().split()
    for word in words:
        word.strip("!.:;,?-/$%()").lower()
        word_list.append(word.strip("!.:;,?-/$%()").lower())
    one_word = {key: 0 for key in words}
    for word in words:
        if word in word_list:
             one_word[word] += 1
        else:
            one_word[word] == 1
    hapaxes=[]
    for x,y in one_word.items():
        if y==1:
            hapaxes.append(x)
    return print(hapaxes)

hapax('Ebook.txt')