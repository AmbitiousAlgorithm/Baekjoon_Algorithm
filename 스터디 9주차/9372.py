T = int(input()) # 테스트 케이스 수
res =[]

for _ in range(T):
    N, M = list(map(int,input().split()))
    for _ in range(M):
        a,b = list(map(int,input().split()))
    res.append(N-1)
print(*res,sep='\n')
