import sys

T = int(input())
answer = []
for _ in range(T):
  case = list(map(int, sys.stdin.readline().split()))
  case.sort(reverse= True)
  answer.append(case[2])

for a in answer:
  print(a)