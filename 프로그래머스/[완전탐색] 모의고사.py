def solution(answers):
    answer = []
    N = len(answers)
    
    A = [1,2,3,4,5]*N
    B = [2,1,2,3,2,4,2,5]*N
    C = [3,3,1,1,2,2,4,4,5,5]*N
    
    a,b,c = 0,0,0
    
    for idx in range(N):
        if answers[idx] == A[idx]:
            a += 1
        if answers[idx] == B[idx]:
            b += 1
        if answers[idx] == C[idx]:
            c += 1
    
    for idx, cnt in enumerate([a,b,c]):
        if cnt == max([a,b,c]):
            answer.append(idx+1)
        
    return sorted(answer)

if __name__ == '__main__':
    print(solution([1,2,1,1]))