import sys

nine = [int(sys.stdin.readline()) for _ in range(9)]
weight = sum(nine)
no, dwarf = 0, 0
nine.sort()

for i in range(9):
  for j in range(i+1, 9):
    suspect = nine[i] + nine[j]
    if weight - suspect == 100:
      if i != j:
        no = i
        dwarf = j
    else:
      continue

del nine[no]
del nine[dwarf-1]

for n in nine:
  print(n)
