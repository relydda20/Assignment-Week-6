def file_line(test):
    currentfile = open(test,'r',encoding = 'utf-8')
    newfile = open('Ebookappended.txt','w', encoding = 'utf-8')
    text = currentfile.readlines()
    i = 1
    for line in text:
        newfile.write(f'{i}. {line}')
        i += 1 
    return(newfile)

file_line('Ebook.txt')