import sys

A, B = map(int, sys.stdin.readline().split())

permutation = []

for i in range(1, B+1):
  print(i)
  for _ in range(i):
    permutation.append(i)

print(sum(permutation[A-1:B]))

