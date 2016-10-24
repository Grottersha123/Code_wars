def del_space_and_commas(p):
    t = []
    k = ''
    for i in p:
        if ' ' in list(i) or ',' in list(i):
            for j in i:
                if j not in ' ,':
                    k+= j
            t.append(k)
            k = ''
        else:
            t.append(i)
    return t
            
            
    
def make_sentences(p):
    # TODO
    return ' '.join(del_space_and_commas(p))+'.'
    
