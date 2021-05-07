import sys
from collections import deque

def valid(x, y, N):
    return 0 <= x < N and 0 <= y < N

def bfs(x, y, DIRECT, N, home):
    visited = []
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        home[x][y] = 0

        for dx, dy in DIRECT:
            nx, ny = dx + x, dy + y
            
            if valid(nx, ny, N) and home[nx][ny] == 1:
                home[nx][ny] = 0
                visited.append((nx,ny))
                queue.append((nx, ny))
    return len(visited) + 1


N = int(sys.stdin.readline())
home = [[0]*N for _ in range(N)]
total = 0
DIRECT = [(-1,0), (0,1), (1,0), (0,-1)]
cnt = []

for i in range(N):
    line = sys.stdin.readline().strip()
    for j, k in enumerate(line):
        home[i][j] = int(k)


for i in range(N):
    for j in range(N):
        if home[i][j] == 1:
            cnt.append(bfs(i,j,DIRECT, N, home))
            total += 1
cnt.sort()

print(total)
for c in cnt:
    print(c)