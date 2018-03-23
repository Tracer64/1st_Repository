#This is all the beginning work for the "dictionary" and how this will make
#counting words in blank space without knowing beforehand very easy.

f = open('data_rev.txt', 'r')
d = {}
for line in f:
    words = line.strip().split()
    #print(line.strip())
    for word in words:
        if word in d:
            d[word] += 1
        else:
            dd[word] = 1

for key in d:
    print( "The word: " + key + " occurs " + str(d[key]) + " times")
