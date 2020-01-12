chk = [0]*30

for _ in range(28):
    num = int(input())
    chk[num-1] = num
# 0인 자리 인덱스를 출력
ans = [i+1 for i,x in enumerate(chk) if x == 0]
print(*ans,sep='\n')
        



