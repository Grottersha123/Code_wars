def solution(a):
    return max([int(a[i:i+5]) for i in range(0,len(a)) ]);
