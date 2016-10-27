def anagrams(word, words):
    #your code here
    w = list(word)
    w.sort()
    y = []
    for i in words:
        t = list(i)
        t.sort()
        if w == t:
            y.append(i)
    return y
        
