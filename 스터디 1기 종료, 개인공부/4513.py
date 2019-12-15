

while(True):
    
    case =  list(map(int,(input().split())))
    
    max_num = max(case)
    case.remove(max_num)

    if (case[0] ==0):
        break

    elif case[0]*case[0] + case[1]*case[1] == max_num*max_num:
        print("right")
    else:
        print("wrong")