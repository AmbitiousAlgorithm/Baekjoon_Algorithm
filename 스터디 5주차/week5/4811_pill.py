# 재귀 호출 문제
N = int(input())
pills = [1]*(N)  # 1은 온전한 알약 0은 반으로 쪼개진 알약
print(pills) # 아예 처음부터 하나를 먹은 상태로 시작한다. 어차피 경우의 수에는 영향을 안미치니까
cnt = 0


# 첫 번째는 무조건 w, 무조건 꺼내져서 하나가 0이 된다. 끝나기 전 마지막은 무조건 반개가 꺼내져서 0이니까 h다.
# def에서는 pill로 받아서 2n-2만큼 돌린다.
def grandpa(pill):
    idx = pills.index(1)
    for _ in range(2*pill-2):
        if pill == pills.count('pill[-1]') and 1 in pills: # 요소들이 다 같으면
            # 1 하나를 꺼내고 -1해서 0으로 바꾸고
            pills[idx] = 0
        if pill == pills.count('pill[-1]') and 0 in pills:
            pills.pop()
        
        elif pill != pills.count('pills[-1]') and 1 in pills:# 요소들이 다르고
            # 1을 꺼냈을때
            if pills.pop() == 1:
                pills[idx] = 0
                grandpa(pill+2)
            # 0을 꺼내면 pop하고 재귀함수
            else:
                pills.pop()
                grandpa(pill-1)
    if not pills:
        return pill
                    



# def(N)하면 
print(grandpa(N))