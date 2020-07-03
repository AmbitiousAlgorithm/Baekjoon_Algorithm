yut = []
res = ['A','B','C','D','E']
ans = []
for _ in range(3):
    case = map(int,input().split(' '))
    yut.append(list(case))

for x in yut:
    for i in range(1,4):
        if x.count(0) == i:
            ans.append(res[i-1])  # 왜 C가 출력이 안될까?
    if x.count(0) ==4 :
        ans.append(res[3])
    elif x.count(1) == 4:
        ans.append(res[-1])
print(*ans,sep='\n')