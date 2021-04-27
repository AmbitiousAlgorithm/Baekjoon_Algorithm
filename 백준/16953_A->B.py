import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())

def bfs(A, B):
    visited = []
    queue = deque()
    queue.append((A,1))

    while queue:
        node, total = queue.popleft()

        if node == B:
            return total
        
        mul, add = node * 2, int(str(node) + "1")
        if mul <= B:
            queue.append((mul, total+1))
        if add <= B:
            queue.append((add, total +1))
            

    return -1

print(bfs(A, B))