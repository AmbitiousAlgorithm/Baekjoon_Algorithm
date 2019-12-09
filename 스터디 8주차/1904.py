import sys
N = int(sys.stdin.readline())

if N ==1:
    print(1)
else:
    a, b = 1,2
    for _ in range(3,N+1):
        a, b = (b) % 15746, (a+b)%15746
    print(b % 15746)




