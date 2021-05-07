import sys
from collections import defaultdict
from collections import deque

N, M, V = map(int,sys.stdin.readline().split())

graph = defaultdict(list)

for _ in range(M):
  node, value = map(int,sys.stdin.readline().split())
  graph[node].append(value)
  graph[value].append(node)



def dfs(graph, V):

  for key in graph:
    graph[key].sort(reverse = True)

  visited = []
  stack = [V]

  while stack:
    number = stack.pop()

    if number not in visited:
      visited.append(number)
      stack.extend(graph[number])
  return ' '.join(map(str,visited))


def bfs(graph, V):
  for key in graph:
    graph[key].sort()
  visited = []
  queue = deque()
  queue.append(V)

  while queue:
    number = queue.popleft()

    if number not in visited:
      visited.append(number)
      queue.extend(graph[number])

  return ' '.join(map(str,visited))

print(dfs(graph, V))
print(bfs(graph, V))
