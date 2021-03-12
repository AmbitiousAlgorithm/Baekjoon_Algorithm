## 문제
- ⚠️ H-index
- 언어 : Ptyhon 3
- https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3


## 풀이
- 

## 코드

[ 정답 코드 ]
```
def solution(citations):
    answer = 0
    
    citations.sort(reverse= True)
    
    for i, citation in enumerate(citations):
        h = len(citations[:i])+1
        if citation >= h:
            answer = h
    
    return answer
```

## 보완점

테스트케이스만 성공. 

🅇 실패한 코드
```
def solution(citations):
    answer = 0
    
    n = len(citations)
    citations.sort(reverse= True)
    
    for i in range(n):
        h = len(citations[:i])+1
        paper = n-h
        if h > paper:
            answer = h
            break
        
    return answer

```

테스트케이스 11,16 실패 
```
def solution(citations):
    h = 0
    
    citations.sort(reverse= True)
    for citation in citations:
        if citation >= h:
            h += 1
        else:
            break
        
    return h
```

## screenshot

<img width="584" alt="스크린샷 2021-01-01 오후 10 46 50" src="https://user-images.githubusercontent.com/35520314/103439799-77d7f300-4c83-11eb-825c-7951fc49a85b.png">



