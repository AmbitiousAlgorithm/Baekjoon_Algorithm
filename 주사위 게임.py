import itertools

def solution(monster, S1, S2, S3):
    cnt = 0
            
    # 경우의 수 리스트 만들기
    cases = list(itertools.product(range(1, S1+1), range(1, S2+1), range(1, S3+1)))
    
    # cases 돌면서 합이 monster일 때 값 체크
    for case in cases:
        if sum(case)+1 not in monster:
            cnt += 1
            
    return int(cnt/len(cases)*1000)