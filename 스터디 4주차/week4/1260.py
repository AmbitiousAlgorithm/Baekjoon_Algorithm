# 1260 DFS와 BFS
import queue
n, m, v = map(int, input().split()) # 정점의 개수, 간선의 개수, 시작 번호

a = [list() for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

for x in a:
    x.sort()
print(a)

def bfs(start):
    q = queue.Queue()
    q.put(start)
    chk[start] = True

    while not q.empty():               
        now = q.get()                 # 큐에서 가장 앞으 노드를 꺼내온다.
        print(now, end=" ")           # 해당 노드를 방문한다는 의미로 출력한다.
        for next in a[now]:           # 방문한 노드의 인접 노드들을 for문을 통해 next에 저장한다.
            if not chk[next]:         # 인접 노드가 체크가 되어있지 않다면
                chk[next] = True      # 체크를 해주고,
                q.put(next)           # 인접 노드를 큐에 넣어준다. 


def dfs(node):
    chk[node] = True
    print(node, end=" ")

    for next in a[node]:
        if not chk[next]:
            dfs(next)

chk = [False]*(n+1)
dfs(v)
print()
chk = [False]*(n+1)
bfs(v)
