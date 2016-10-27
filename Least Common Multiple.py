import functools as f
def lcmtwo(a,b):
    m = a*b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a+b)

def lcm(*args):
    t = 1
    for i in args:
        print(t)
        t = lcmtwo(t,i)
    return t
      
