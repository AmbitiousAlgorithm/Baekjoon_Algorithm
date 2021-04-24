import sys
from collections import deque
from collections import Counter

N, M =  map(int, sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split()[0])) for _ in range(N)]

direction = [(-1,0), (1,0), (0,-1), (0,1)]

def valid(x, y ,n , m):
    return 0<= x < n and 0<= y < m

queue = deque()
queue.append((0,0))
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1
    
while queue:
    x, y = queue.popleft()

    for dx, dy in direction:
        next_x, next_y = dx + x, dy + y
        if not valid(next_x, next_y, N, M):
            continue
        if visited[next_x][next_y] == 0 and graph[next_x][next_y] == 1:
            visited[next_x][next_y] = visited[x][y] + 1
            queue.append((next_x, next_y))
print(visited[N-1][M-1])
