N = int(input())
rope =[]
w = 0

for i in range(N):
    rope.append(int(input()))
rope.sort(reverse=True)

for i in range(N):
    tmp = rope[i]*(i+1)
    if tmp > w:
        w = tmp
        print(w)

print(w)





