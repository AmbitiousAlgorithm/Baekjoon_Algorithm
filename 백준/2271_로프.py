N = int(input())
weight = []
for _ in range(N):
    weight.append(int(input()))

weight.sort(reverse=True)
w = 0


for k in range(N):
    tmp = weight[k]*(k+1)
    if tmp > k:
        w = tmp
print(w)
