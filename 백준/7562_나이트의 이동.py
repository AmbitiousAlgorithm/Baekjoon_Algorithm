import sys
from collections import deque
def valid(x, y, I):
    return 0 <= x < I and 0 <= y < I

def bfs(x,y, visited, DIRECT, tx,ty, I):
    queue = deque()
    queue.append((x,y, 0))
    visited[x][y] = 1

    while queue:
        x, y, level = queue.popleft()

        if x == tx and y == ty:
            return level
            break

        for dx, dy in DIRECT:
            nx, ny = dx + x, dy + y

            if valid(nx, ny, I) and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny, level+1))

T = int(sys.stdin.readline())
case = []
for _ in range(T):
    I = int(sys.stdin.readline())
    x,y = map(int, sys.stdin.readline().split())
    tx, ty = map(int, sys.stdin.readline().split())
    
    DIRECT = [(-2,-1), (-2,1), (-1,2), (-1,-2), (1,2), (2,1), (1,-2), (2,-1)]
    visited = [[0]*I for _ in range(I)]
    
    case.append(bfs(x,y, visited, DIRECT, tx,ty, I))

for c in case:
    print(c)

