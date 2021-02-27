## 문제
- ⚠️ 크레인 인형 뽑기 게임
- 언어 : Ptyhon 3
- https://programmers.co.kr/learn/courses/30/lessons/64061


## 풀이
- 이중리스트 합치기로 각 열마다 인형을 추합한다.
- board[move-1] 에서 0이 아닌 값을 만나면 값을 리턴하고 0으로 변경한다.
- None(모든 배열이 0인 경우)이 아니면 stack에 넣고
- stack이 2개 이상일 떄 맨 위 2개 값을 검사해서 같은 값이면 pop 2번해서 제거하고 answer += 2

## 코드

[ 정답 코드 ]
```
def dolls(move, board):
    for idx in range(len(board[move-1])):
            if board[move-1][idx] != 0:
                doll = board[move-1][idx]
                board[move-1][idx] = 0
                
                return doll

def solution(board, moves):
    answer = 0

    # 이중 리스트 합치기
    board = list(map(list, zip(*board)))
    stack = []
    
    for move in moves:
        doll = dolls(move, board)
        if doll is not None: # None이 아니면 append
            stack.append(doll)
            if len(stack) > 1:
                if stack[-1] == stack[-2]:
                    answer += 2
                    stack.pop()
                    stack.pop()
                    
    return answer

```

## 보완점

처음에는 def dolls()에 있던 for문을 함수로 뺴지 않고 안에 넣었었는데, 통과하지 못헀다.
그 이유는 for문을 돌면서 board[move-1]에 있는 인형들을 다 0으로 만들고나서야 for문이 끝나기 떄문이었다.
따라서 함수로 빼서 0이 아닌 값을 만나면 리턴하고 종료시키고,
stack에 추가해서 확인하였다.

🅇 실패한 코드
```

def solution(board, moves):
    answer = 0

    # 이중 리스트 합치기
    board = list(map(list, zip(*board)))
    stack = []
    
    for move in moves:
        for idx in range(len(board[move-1])):
            if board[move-1][idx] != 0:
                doll = board[move-1][idx]
                stack.append(doll)
                board[move-1][idx] = 0

            if len(stack) > 1:
                if stack[-1] == stack[-2]:
                    answer += 2
                    stack.pop()
                    stack.pop()
                    
    return answer

```


## screenshot


<img width="590" alt="스크린샷 2021-02-27 오후 11 33 45" src="https://user-images.githubusercontent.com/35520314/109390541-9e4d9e00-7955-11eb-8ee2-1a36961440a4.png">


