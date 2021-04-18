import sys

N = int(input())
case = map(int, sys.stdin.readline().split())
cnt = 0


def sieve(n):
  if n <= 1:
    return False
  num = 2

  while num*num <= n:
    if n % num == 0:
      return False
    num += 1
  return True


for num in case:
  if sieve(num):
    cnt += 1

print(cnt)
