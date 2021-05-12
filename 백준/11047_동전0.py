import sys

N, K = map(int, sys.stdin.readline().split())
case = []
for _ in range(N):
    case.append(int(sys.stdin.readline()))
case.sort(reverse=True)

answer = 0

for coin in case:
    if coin > K:
        continue
    div, mod = divmod(K, coin)
    answer += div
    K = mod

print(answer)
    
