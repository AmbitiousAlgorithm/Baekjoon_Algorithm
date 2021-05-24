```
from collections import deque

def valid(x,y,n,m):
    return 0 <= x < m and 0 <= y < n

def bfs(x, y, graph, target):
    visited = [[0]*3 for _ in range(4)]
    queue = deque()
    queue.append((x, y, 0))
    
    while queue:
        x, y, level = queue.popleft()
        visited[x][y] = 1
        
        if graph[x][y] == target:
            return level
            break
        
        for dx, dy in [(-1,0), (0,1), (1,0), (0,-1)]:
            nx, ny = dx + x, dy + y
            
            if valid(nx,ny,3,4) and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny, level +1))
                
def find_index(graph, num):
    for i in range(4):
        if num in graph[i]:
            return i, graph[i].index(num)
    

def solution(numbers, hand):
    answer = ''
    
    l = '*'
    r = '#'
    graph = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]

    for number in numbers:
        if number in [1,4,7]:
            answer = answer + 'L'
            l = number
        elif number in [3,6,9]:
            answer = answer + 'R'
            r = number
        else:
            left = bfs(*find_index(graph, l), graph, number)
            right = bfs(*find_index(graph, r), graph, number)

            if left > right:
                answer = answer + 'R'
                r = number
            elif left < right:
                answer = answer + 'L'
                l = number
            elif left == right:
                answer = answer + hand[0].upper()
                if hand[0].upper() == 'R':
                    r = number
                else:
                    l = number
            
    return answer
```