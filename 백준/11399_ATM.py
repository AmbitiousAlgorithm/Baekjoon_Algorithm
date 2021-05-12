import sys

N = int(input())
case = map(int, sys.stdin.readline().split())
# time DESC
case.sort()

answer = 0

for i in range(N):
    for j in range(0, i+1):
        answer += case[j]
print(answer)

# sum = case[0]

# for i in range(len(case)-1):
#     c = case[i] + case[i]+1
#     sum += c
#     case[i] = case[i+1]
#     case[i+1] = c
# print(sum)