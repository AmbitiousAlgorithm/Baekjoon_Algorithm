import math
import copy
import collections
def solution(progresses, speeds):
    prog = collections.deque([math.ceil((100-progress)/speed) for progress,speed in zip(progresses,speeds)])
    answer = []
    while len(prog) > 0 :
        tmp = prog.popleft()
        cnt = 1
        for i in copy.deepcopy(prog) :
            if tmp < i :
                break
            prog.popleft()
            cnt += 1
        answer.append(cnt)
    return answer

print(solution([93,30,55,50,89],[1,30,5,25,1]))
