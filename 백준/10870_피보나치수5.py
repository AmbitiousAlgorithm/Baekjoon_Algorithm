import sys

n = int(sys.stdin.readline())

def fib(n):
  if n == 1 or n == 2:
    return 1
  elif n == 0:
    return 0
  else:
    return fib(n-2) + fib(n-1)

print(fib(n))