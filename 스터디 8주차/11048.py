n,m = map(int,(input().split()))

candy = [[0]*(m+1)]


for _ in range(n):
    x = list(map(int, input().split()))
    candy.append([0]+x)


for x in range(1,n+1): #2, 1, 0
    for y in range(1,m+1): #2,1,0
        candy[x][y] += max(candy[x-1][y-1],max(candy[x-1][y],candy[x][y-1]))
        
    
print(candy[n][m])