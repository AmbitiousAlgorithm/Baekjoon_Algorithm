
#  queue = deque([(infest)for infest in tuple(map(tuple,infests))])
    
#     visited = [[False]* n for _ in range(m)] # 지나간 자리 검사하는 배열
#     DELTAS = ((0,1),(0,-1),(1,0),(-1,0)) 
    
#     def valid(x, y, m, n):
#         return 0 <= x < m and 0 <= y < n
    
#     while queue:
#         print(queue)
#         x,y = queue.popleft()
#         print(x,y)
#         for dx, dy in DELTAS:
#             next_x = x + dx
#             next_y = y + dy
            
#             if valid(next_x, next_y, m, n) and [next_x, next_y] not in vaccinateds and queue:
#                 print((next_x, next_y))
#                 queue.append((next_x, next_y)) # 감염자 추가
#                 visited[next_x][next_y] = True # 방문 체크
#                 print(visited)
                
#     # for x in range(m):
#     #     for y in range(n):
#     #         visited[i][j] = True # 백신이면 그냥 true로 체크하고 넘어간다.
#     #         bfs(m, n, x, y, infests, vaccinateds, visited)
#     #         answer += 1

            
                
#     # 처음부터 다 백신 다 감염인 경우
#     if len(infests) == len(vaccinateds) == m == n:
#         return 0