a = {'H': 'U', 'z': 'm', 'Q': 'D', 'd': 'q', 'F': 'S', 'k': 'x', 's': 'f', 'U': 'H', 'a': 'n', 'C': 'P', 'J': 'W', 'o': 'b', 'l': 'y', 'M': 'Z', 'B': 'O', 'G': 'T', 'e': 'r', 'I': 'V', 'R': 'E', 'Z': 'M', 'v': 'i', 'P': 'C', 'E': 'R', 'i': 'v', 'j': 'w', 'A': 'N', 'm': 'z', 'p': 'c', 'X': 'K', 'K': 'X', 'x': 'k', 'r': 'e', 'L': 'Y', 't': 'g', 'u': 'h', 'Y': 'L', 'D': 'Q', 'y': 'l', 'S': 'F', 'N': 'A', 'T': 'G', 'h': 'u', 'n': 'a', 'V': 'I', 'f': 's', 'O': 'B', 'W': 'J', 'w': 'j', 'c': 'p', 'q': 'd', 'b': 'o', 'g': 't'}

def rot13(m):
    #your code here
    r = ''
    for i in m:
        if i  not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            r+= i
        else:
            r+= a[i]
    return r
