from collections import deque
import heapq

def solution(brown, red):
    answer = []
    
    # red의 약수 구하기
    def sieve(n):
        prime = [True]*(n+1)
        prime[0] = False
        prime[1] = False
        
        for candidate in range(2, n+1):
            for multiple in range(candidate*candidate, n+1, candidate):
                prime[multiple] = True
        result = [idx for idx, val in enumerate(prime) if val]
        if not result:
            result = [1]
        return result
    
    # 소수 중에서 약수 구하기
    def divisor(red):
        return  [(prime, red // prime) for prime in sieve(red) if red % prime == 0]
    
    # 짝지어서 더한 값이 (brown-4)/2 와 같으면 x+2,y+2 반환
    for i in divisor(red):
        if sum(i) == (brown-4)/2:
            x, y = i
            if x > y or x == y:
                answer = [x+2,y+2]
    
    return answer