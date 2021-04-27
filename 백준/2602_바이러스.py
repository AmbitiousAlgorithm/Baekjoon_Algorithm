import sys
from collections import defaultdict

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

graph = defaultdict(list)
for _ in range(K):
    node, value = map(int, sys.stdin.readline().split())
    graph[node].append(value)
    graph[value].append(node)


def dfs(graph, V):
    visited = []
    stack = [V]

    while stack:
        node = stack.pop()

        if len(visited) == N:
            break
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited


print(len(dfs(graph, 1))-1)
