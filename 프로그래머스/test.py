from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    # 100 - progresses를 하고 speeds로 나눈 뒤 올림해준다.
    progresses = list(map(lambda x,y: math.ceil((100-x)/y),progresses,speeds))
    # 기준 값
    release =  deque()
    
    for i in range(len(progresses)):
        release.append(progresses[i])
        if release[0] > progresses[i]:
            answer.append(len(release))
            release.clear()

    answer.append(len(release))
                  
    return answer

print(solution([93,30,55,50,89],[1,30,5,25,1]))
