import sys

num, k = (map(int, sys.stdin.readline().split()))

divisor = [n for n in range(1, num+1) if num % n == 0]

if len(divisor) < k:
  print(0)
else:
  print(divisor[k-1])