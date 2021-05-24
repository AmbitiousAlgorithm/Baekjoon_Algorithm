
from collections import deque

def solution(number, k):
    answer = ''    
    MAX = [number[0]]

    for num in number[1:]:  
        while MAX and MAX[-1] < num and k > 0:
            MAX.pop()
            k -= 1
        MAX.append(num)
    
    while k > 0:
        MAX.pop()
        k-=1
        
    return ''.join(MAX)
