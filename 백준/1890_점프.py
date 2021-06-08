import sys

N = int(sys.stdin.readline())

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

DIRECT = [(0,1), (1,0)]

table = [[0]*N for _ in range(N)]
table[0][0] = 1

def valid(x, y):
    return 0 <= x < N and 0 <= y < N

for x in range(N):
    for y in range(N):
        move = graph[x][y]

        if (x,y) == (N-1, N-1): # 첨에 graph[x][y] == 0으로 했는데, graph 값에 도착지점 말고도 0이 있을 수 있었다는 반례.
            print(table[N-1][-1])
            break

        for dx, dy in DIRECT:  # dx, dy 돌면서 누적
            nx, ny = dx*move + x, dy*move + y
            if valid(nx, ny):
                table[nx][ny] += table[x][y] # 이동하기 이전 값 누적
            

