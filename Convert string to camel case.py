def conver_to_list(lst):
    t = ''
    y = []
    for i in lst:
        if i == '-' or i == '_':
            y.append(t)
            t = ''
            continue
        else:
            t+=i
    y.append(t)
    return y
def to_camel_case(text):
    #your code here
    text = conver_to_list(text)
    t = text[0]
    for i in range(1,len(text)):
        t+=text[i].capitalize()
    return t
        
        
        
