N = int(input())
res = []

for _ in range(N):
    res.append(int(input()))

cnt = res.count(0)
if cnt > len(res)/2:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")