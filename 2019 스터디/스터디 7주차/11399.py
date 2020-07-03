N = int(input())
case = list(map(int,input().split()))
case.sort()
sum = case[0]


for i in range(len(case)-1):
    c = case[i]+case[i+1]
    sum = sum + c
    case[i] = case[i+1]
    case[i+1] = c

print(sum)




    

