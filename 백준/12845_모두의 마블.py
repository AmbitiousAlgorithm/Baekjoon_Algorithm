import sys


n = int(sys.stdin.readline())
cards =list(map(int, sys.stdin.readline().split()) )

MAX = 0

for idx, card in enumerate(cards):
    gold = 0
    for i, last in enumerate(cards):
        if i != idx:
            gold += card + last
    if MAX < gold:
        MAX = gold
print(MAX)

