import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())

graph = [list(sys.stdin.readline().split()[0]) for _ in range(M)]
visited = [[0]*N for _ in range(M)] 
direct = [(-1,0), (1,0), (0,-1), (0,1)]
queue = deque()
W, B = 0, 0

def valid(x, y, n, m):
  return 0 <= x < m and 0 <= y < n

def bfs(x, y, soldier):
  cnt = 1
  queue.append((x, y))
  visited[x][y] = 1

  while queue:
    x, y = queue.popleft()

    for dx, dy in direct:
      next_x, next_y =  x + dx, y + dy

      if valid(next_x, next_y, N, M) and visited[next_x][next_y] == 0 and graph[next_x][next_y] == soldier:
        queue.append((next_x, next_y))
        visited[next_x][next_y] = 1
        cnt += 1

  return cnt


for i in range(M):
  for j in range(N):
    if visited[i][j] == 0:
      if graph[i][j] == 'W':
        W += bfs(i,j, 'W') ** 2
      elif graph[i][j] == 'B':
        B += bfs(i,j, 'B') ** 2

answer = [W,B]
print(' '.join(map(str,answer)))

# from collections import deque

# def bfs(y, x):
#     q = deque()
#     q.append((y, x))
#     c = graph[y][x]

#     graph[y][x] = 1
#     cnt = 0
#     while q:
#         y, x = q.popleft()
#         cnt += 1
#         for dy, dx in d:
#             Y, X = y+dy, x+dx
#             if (0 <= Y < M) and (0 <= X < N) and graph[Y][X] == c:
#                 q.append((Y, X))
#                 graph[Y][X] = 1
#     return cnt

# N, M = map(int, input().split())
# graph = [list(input()) for _ in range(M)]
# d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# w = b = 0
# for i in range(M):
#     for j in range(N):
#         if graph[i][j] == 'W':
#             w += bfs(i, j)**2
#         elif graph[i][j] == 'B':
#             b += bfs(i, j)**2
# print(w, b)