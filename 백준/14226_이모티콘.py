import sys
from collections import deque

S = int(sys.stdin.readline())
MAX_SIZE = 1001
visited =  [[False for _ in range(MAX_SIZE)] for _ in range(MAX_SIZE)]

def valid(x,y):
    return 0<=y < MAX_SIZE and 0<=x < MAX_SIZE and not visited[x][y]

def bfs():
    queue = deque()
    CLIP, SCREEN, TIME = 0,1,0
    queue.append((SCREEN, CLIP, TIME))
    visited[SCREEN][CLIP] = True

    while queue:
        screen, clipboard, time = queue.popleft()

        if screen == S:
            return time
            break

        next_ = screen
        if not visited[screen][next_]:
            visited[screen][next_] = True
            queue.append((screen, next_, time+1))

        if clipboard > 0:
            next_ = screen + clipboard
            if valid(next_, clipboard):
                visited[next_][clipboard] = True
                queue.append((next_, clipboard, time+1))
        
        if screen > 1:
            next_ = screen - 1
            if valid(next_, clipboard):
                visited[next_][clipboard] = True
                queue.append((next_, clipboard, time+1))

    
print(bfs())

