# A x B x C 계산한 결과 숫자가 몇번씩 쓰였는지?
# from collections import Counter

A = int(input())
B = int(input())
C = int(input())

mul = A*B*C
res = list(str(mul))  # 곱하기 결과 리스트
for i in range(10): # 곱한 결과 길이만큼+2
    cnt = res.count(str(i))  # 개수 세서 출력하기 i는 0부터 시작하니까
    print(cnt)



