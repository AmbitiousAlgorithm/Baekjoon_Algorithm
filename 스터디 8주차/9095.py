
T = int(input())
case =[1,2,4]

for i in range(T):
    n = int(input())
    for x in range(3,10):
        cas = case[i-1]+case[i-2]+case[i-3]
        case.append(cas)

    print(case[n-1])