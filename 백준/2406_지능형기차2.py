import sys

station = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
train = 0
max_val = []

for i in range(len(station)):
  train += station[i][1] - station[i][0]
  max_val.append(train)

print(max(max_val))
  


