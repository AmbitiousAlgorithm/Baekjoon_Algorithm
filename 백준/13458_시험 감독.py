import sys

N = int(sys.stdin.readline())
room = map(int,sys.stdin.readline().split())
B, C = map(int,sys.stdin.readline().split())


# room.sort()
person = N

case = list(map(lambda x: x-B, room))

for last in case:
    if last > 0:
        if last % C:
            person += (last // C) + 1
        else:
            person += (last // C)

print(person)
