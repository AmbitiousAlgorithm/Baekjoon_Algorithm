## 문제
- ⚠️ 해시 Lv1. 완주하지 못한 선수
- 언어 : Ptyhon 3
- https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3


## 풀이
- python 모듈 collections으로 푸는 것이 정석
- 이게 왜 hash 문제로 들어와있는지 의문, 해시로 풀려다가 효율성 테스트에서 실패
- hash로 풀려면, hash 내장함수 사용

## 코드

[ 정답 코드 ]
```
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
```
[ 통과한 다른 사람 코드 ]
```
result = {}

def solution(participant, completion):
    for a in participant:
        result[a] = result.get(a, 0) + 1

    for b in completion:
        result[b] -= 1
        if result[b] == 0:
            del result[b]
    return list(result.keys())[0]
```

## 보완점

hash로 풀지 못한 점. 오랜만에 알고리즘을 쉬고 하려니 간단한 문제임에도 많이 헤맸다.<br>
내가 제대로 푼 게 아니라 참고한 코드로 통과한 점이 많이 아쉽다.<br>
python 라이브러리를 많이 공부해보자!


[ 🆇 시도한 코드 ]
```
def solution(participant, completion):
    hash ={}
    cnt =0
    answer = ''
    
    for i in participant:
        hash[cnt] = i
        cnt +=1
        
    for p in completion:
        for j in list(hash.keys()):
            if p==hash[j]:
                del hash[j]
            else:
                answer = hash[j]
            
    return answer
```
👉동명이인을 뽑아내지 못함, 테스트 케이스 통과 못함.


## screenshot
<img width="589" alt="스크린샷 2020-07-03 오후 5 54 18" src="https://user-images.githubusercontent.com/35520314/86454894-df57c900-bd5a-11ea-96a7-9a75f9bb3743.png">


