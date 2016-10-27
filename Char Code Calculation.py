def calc(x):
    # your code here
    t = ''
    t1 = ''
    for i in x:
        t+= str(ord(i)).replace('7','1')
    for i in x:
        t1+= str(ord(i))
    return abs(sum(list(map(int,list(t))))-sum(list(map(int,list(t1)))))
    
        
