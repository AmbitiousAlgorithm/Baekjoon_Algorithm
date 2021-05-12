import sys
import heapq

# 그냥 풀어서는 안됨. 시간초과가 뜬다.

N = int(sys.stdin.readline())
classes = []
for _ in range(N):
    S, T = map(int, sys.stdin.readline().split())
    classes.append((S,T))
# 수업 시작이 일찍 되는 순서대로 정렬해야한다.
classes = sorted(classes, key=lambda x:x[0])

queue = []

for c in classes:
    if queue and queue[0] <= c[0]:
        heapq.heappop(queue)
    heapq.heappush(queue, c[1])

print(len(queue))

