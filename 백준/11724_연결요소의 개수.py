import sys
from collections import defaultdict
sys.setrecursionlimit(10000)

def dfs(V):
    stack = [V]

    while stack:
        number = stack.pop()

        if visited[number] == 0:
            visited[number] = 1
            stack.extend(graph[number])

N, M = map(int,sys.stdin.readline().split())

graph = defaultdict(list)
visited = [0]* (N+1)
cnt = 0

for _ in range(M):
    node, value = map(int,sys.stdin.readline().split())
    graph[node].append(value)
    graph[value].append(node)


for node in range(1, N+1):
    if visited[node] == 0:
        dfs(node)
        cnt += 1

print(cnt)





        
