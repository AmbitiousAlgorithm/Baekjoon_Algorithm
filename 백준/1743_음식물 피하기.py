import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
graph = [[0]*M for _ in range(N)]

for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    graph[x-1][y-1] = 1

def valid(x, y, n, m):
    return 0<= x < n and 0<= y < m

def bfs(x,y,visited):
    cnt = 0
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        direction = [(-1,0), (1,0), (0,-1), (0,1)]

        for dx, dy in direction:
            next_x, next_y = dx + x, dy + y
            
            if valid(next_x, next_y, N, M) and not visited[next_x][next_y] and graph[next_x][next_y] == 1:
                visited[next_x][next_y] = True
                queue.append((next_x, next_y))
                cnt += 1
    return cnt


visited = [[False]*M for _ in range(N)]
answer = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            answer.append(bfs(i,j,visited))

print(max(answer))