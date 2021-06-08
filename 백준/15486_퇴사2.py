import sys

N = int(sys.stdin.readline())

time, price = [], []

for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    time.append(t)
    price.append(p)

answer = [0]*(N+1)
MAX = 0

for i in range(N):
    MAX = max(MAX, answer[i])

    if i + time[i] > N:
        continue
    answer[i+time[i]] = max(answer[i+time[i]], MAX + price[i])

print(max(answer))

