import sys

def valid(x,y,n,m):
    return 0<= x < m and 0<= y< n

def dfs(start, garden):
    DIRECT = [(-1,0), (1,0), (0,-1), (0,1)]
    stack = []
    stack.append(start)

    while stack:
        y, x = stack.pop()
        garden[y][x] = 0

        for dy, dx in DIRECT:
            next_y, next_x = y + dy, x + dx

            if valid(next_x, next_y,N,M) and garden[next_y][next_x] == 1:
                stack.append((next_y, next_x))
                garden[next_y][next_x] = 0


T = int(input())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    
    garden = [[0]*M for _ in range(N)]
    cnt = 0
    
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        garden[y][x] = 1

    for x in range(M):
        for y in range(N):
            if garden[y][x] == 1:
                dfs((y,x), garden)
                cnt += 1

    print(cnt)