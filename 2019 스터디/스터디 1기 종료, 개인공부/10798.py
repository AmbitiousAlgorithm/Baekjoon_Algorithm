## 세로 출력(구현문제)

# 2차원 배열로 입력받기 
matrix = [[0]*5 for _ in range(5)]

for i in range(5):
  arr = list(input())
  arrlen = len(arr)
  for j in range(arrlen):
    matrix[i][j] = arr[j]

# 세로로 출력
for i in range(15):
  for j in range(5):
    if matrix[j][i] == 0:
      continue
    else:
      print(matrix[j][i],end='')
