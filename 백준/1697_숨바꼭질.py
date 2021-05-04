import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
MAX_SIZE = 1000001

def valid(x):
    return 0 <= x < MAX_SIZE

def bfs(X,K):
    visited = [0] * MAX_SIZE
    queue = deque()
    queue.append((X,0))

    while queue:
        location, time = queue.popleft()
        visited[location] = 1

        if location == K:
            return time
            break

        for move in [location-1, location+1, 2*location]:
            if valid(move) and visited[move] == 0:
                queue.append((move, time +1))
    return min_time

print(bfs(N, K))