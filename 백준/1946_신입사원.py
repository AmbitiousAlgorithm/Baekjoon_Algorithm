import sys

def num(cases, N):
    cases.sort(key = lambda x:x[0])
    people = 1
    min = cases[0][1]

    for case in cases[1:]:
        if case[1] < min:
            min = case[1]
            people += 1
    return people

T = int(sys.stdin.readline())
answer = []
for _ in range(T):
    N = int(sys.stdin.readline())
    cases = []
    cases = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    answer.append(num(cases, N))

for a in answer:
    print(a)



