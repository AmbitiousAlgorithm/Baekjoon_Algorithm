N,K = map(int,input().split())
money = []
coin = 0

for i in range(N):
    money.append(int(input()))

for i in range(1,N+1):
    if (K // money[-i] !=0):
        coin += K // money[-i]
        K %= money[-i]

print(coin)