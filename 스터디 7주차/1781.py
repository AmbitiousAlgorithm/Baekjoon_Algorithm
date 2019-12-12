N = int(input())
case = []
cupnoodle = []

for i in range(N):
    dead,cup = map(int,input().split())
    case.append((dead,cup))

case.sort()

for i in range(1,N+1):
    deadline = case[i-1][0]
    cupnoodle.append(case[i-1][1])

    while (deadline < len(cupnoodle)):
        cupnoodle.remove(min(cupnoodle))

if cupnoodle:
    result = sum(cupnoodle)
print(result)