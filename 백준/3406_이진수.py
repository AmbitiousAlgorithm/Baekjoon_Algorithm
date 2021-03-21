import sys

T = int(input())
decimal = [int(sys.stdin.readline()) for _ in range(T)]

def div(num):
  return divmod(num, 2)

for dec in decimal:
  binary = []
  while dec != 1:
    q,r = div(dec)
    binary.append(r)
    dec = q
  binary.append(dec)
  answer = list( map(str, filter(lambda x: binary[x] == 1, range(len(binary)))))
  print(' '.join(answer))
