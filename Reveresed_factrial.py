#обратный фаториал!!
def reverse_factorial(num):
    # happy coding
    ind = 1
    if num % 2 != 0:
        return 'None'
    else:
        while True:
            
            if num == 1:
                return str(ind-1) + '!'
            
            if num %ind == 0:
                num = num // ind
                ind +=1
            else:
                return 'None'
            
            
