def revword(word):
    word=word[::-1].lower()
    return word

#filr=open("C:/Users/barab/anaconda3/pkgs/python-3.8.3-he1778fa_2/Scripts/text.txt")
def countword():
    filr = open("C:/Users/barab/anaconda3/pkgs/python-3.8.3-he1778fa_2/Scripts/text.txt")
    dict1={}
    first_word = None
    for w in filr:
        w=w.split()
        dict1[w[0]] = 1
        for word in w:
            if first_word is None:
                first_word = word
        for x in w:
             x = revword(x)
             if x in dict1:
                dict1[x] += 1
             else:
                dict1[x]=1
    return dict1.get(first_word, 0)
print(countword())
