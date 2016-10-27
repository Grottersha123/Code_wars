
    # write the function is_anagram
def is_anagram(te, oo):

    t = list(te.lower())
    t.sort()
    o = list(oo.lower())
    o.sort()
    if t == o:
        return  "The word " +  te + "is an anagram of " + oo 
    return False
