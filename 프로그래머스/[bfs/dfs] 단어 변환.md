## 문제
- ⚠️ 단어 변환
- 언어 : Ptyhon 3
- https://programmers.co.kr/learn/courses/30/lessons/43163#qna


## 풀이
- bfs로 시작단어와 level을 넣고 
- compare 함수로 한 글자만 다른 단어들의 리스트를 만든 다음
- 그 리스트를 순회하면서 다시 큐에 넣는다.
- 리스트 안에 target 단어가 있으면 바로 level 리턴하고 종료

## 코드

[ 정답 코드 ]
```
from collections import deque

# 현재 노드에서 갈 수 있는 인접 노드들
def compare(current, word):
    cnt = 0
    for idx, letter in enumerate(word):
        if letter == current[idx]:
            cnt += 1
    if cnt == len(current)-1:
        return True
    else:
        return False
    
def bfs(begin, target, words):
    queue = deque()  # 시작노드 넣기
    queue.append((begin, 0))
                 
    while queue:
        current, level = queue.popleft() # 노드를 하나 호출해서

        # target과 같으면 break
        if current == target:
            return level
            break

        # 한 글자만 다른 인접 노드들의 리스트를 뽑아서
        next_node = [word for word in words if compare(current, word)]

        # 이 리스트를 순회하면서 visited하지 않았으면 노드를 queue에 넣고 visited 체크해준다.
        for node in next_node:
            queue.append((node, level+1))
            

    
def solution(begin, target, words):
                 
    # target이 words안에 없으면 0 반환
    if target not in words:
        return 0
    
    answer = bfs(begin, target, words)
    
    return answer
```

## 보완점


🅇 실패한 코드

if letter in current로 작업했었는데, 테스트 케이스 3번이 통과가 되지 못했다. 반례를 찾아보니,
aaa, aab를 비교하는 경우 a in aab 해버리면 개수인 2가 반환되는 것이 아니라 3이 되어서 이 케이스를 true로 잡아내지 못하는 거였다.
그래서 letter랑 current[idx]로 글자를 하나하나 짚어나가는 것으로 수정하니 통과.

```
from collections import deque


def compare(current, word):
    cnt = 0
    for letter in word:
        if letter in current:
            cnt += 1
    if cnt == len(current)-1:
        return True
    else:
        return False
    
def bfs(begin, target, words):
    queue = deque()
    queue.append((begin, 0))
                 
    while queue:
        current, level = queue.popleft()

        if current == target:
            return level
            break

        next_node = [word for word in words if compare(current, word)]

        for node in next_node:
            queue.append((node, level+1))

```


## screenshot

<img width="584" alt="스크린샷 2021-01-01 오후 10 46 50" src="https://user-images.githubusercontent.com/35520314/103439799-77d7f300-4c83-11eb-825c-7951fc49a85b.png">



