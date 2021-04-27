import sys
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
MAX_SIZE = 1000001

def valid(step):
    return 0<= step < MAX_SIZE

def bfs(N,K):
    min_time, way = 0, 1
    queue = deque()
    queue.append((N,0)) # time
    visited = [0]*MAX_SIZE

    while queue:
        location, time = queue.popleft()
        visited[location] = 1

        if location == K:
            min_time += time
            way += 1
            break
            
        for step in [location*2, location-1, location+1]:
            if valid(step) and visited[step] == 0 :
                queue.append((step, time+1))
    print(min_time)
    print(way)

bfs(N,K)
