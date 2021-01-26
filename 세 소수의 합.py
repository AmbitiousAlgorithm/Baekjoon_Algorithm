from itertools import combinations

def solution(n):
    answer = 0
    
    # 어쨌든 n 보다는 작은 수의 소수들로 이루어짐(에라토스테스트의 체)
    def sieve(n):
        is_prime = [True] * (n+1)
        is_prime[0] = False
        is_prime[1] = False
        
        for candidate in range(2, n+1):
            if not is_prime[candidate]:
                continue
            for multiple in range(candidate*candidate, n+1, candidate):
                is_prime[multiple] = False

        return [idx for idx, val in enumerate(is_prime) if val]
    
    candidates = sieve(n)
    
    
    # 3개의 합 경우의 수 구하기(3개 조합)
    candidates_list = list(combinations(candidates,3))
    for candidate in candidates_list:
        if sum(candidate) == n: # 중에서 합이 n이면 
            answer += 1
    

    return answer