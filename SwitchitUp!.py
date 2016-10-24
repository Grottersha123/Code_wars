number = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
def switch_it_up(n):
    #your code here
    return number[n]
"""
Round any given number to the closest 0.5 step

I.E.

solution(4.2) = 4
solution(4.3) = 4.5
solution(4.6) = 4.5
solution(4.8) = 5
Round up if number is as close to previous and next 0.5 steps.

solution(4.75) == 5

here we should use the formule round(n/0.5)*0.5
"""
def solution(n):
    
    return round(n/0.5)*0.5
