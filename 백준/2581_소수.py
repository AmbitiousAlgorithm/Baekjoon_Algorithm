M = int(input())
N = int(input())


def sieve(n):
  if n <= 1:
    return False
  num = 2

  while num*num <= n:
    if n % num == 0:
      return False
    num += 1
  return True
  # prime = [True] * (n+1)
  # prime[0] = False
  # prime[1] = False

  # for num in range(2, n+1):
  #   if not prime[num]:
  #     continue
  #   for multiple in range(num*num, n+1, num):
  #     prime[multiple] = False
  # return [idx for idx, value in enumerate(prime) if value]

# answer = set(sieve(N)) - set(sieve(M))

sum, min = 0, 0

for num in range(M, N+1):
  if sieve(num):
    if min == 0:
      min = num
    sum += num

if sum == 0:
  print(-1)
else:
  print(sum)
  print(min)
  # print(sum(answer))
  # print(min(answer))

