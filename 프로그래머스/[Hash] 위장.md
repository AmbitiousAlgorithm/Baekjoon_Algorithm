## 문제
- ⚠️ 해시 Lv2. 위장
- 언어 : Ptyhon 3
- https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3


## 풀이
- 각각 옷 종류인 딕셔너리의 values 값을 count
- 옷 종류를 안입거나,입거나 하는 경우로 나누어 (옷 종류 +1)씩 경우의 수가 생긴다.
- 종류 별로 곱한 다음 아무것도 안입는 경우를 -1해서 리턴

## 코드

[ 정답 코드 ]
```
from collections import Counter

def solution(clothes):
    answer = 1
    
    # 이중리스트 -> 딕셔너리 변환
    clothes = dict(zip(list(map(list,zip(*clothes)))[0],list(map(list,zip(*clothes)))[1])) # key: 실제 옷 , value: 종류
    val = list(clothes.values())
    l = {}

    # value 개수 세기
    for i in val:
        l[i]=val.count(i)
        
    for k in list(l.values()):
        answer *= (k+1)
    return answer-1
```

## 보완점

[ 🆇 시도한 코드 ]
```
없음.
```
👉 처음엔 조합으로 하는 줄알고 itertools에서 조합을 사용하여 시도해보았다. 하지만 원하는 대로 나오지않고 딕셔너리로 변환해서 하려니 시간도 오래걸렸다. 물론 hash니까 딕셔너리로 풀어보는게 좋지만, 실제로 풀어보는 느낌처럼 리스트로 막 푸는 것이 더 좋을 것이란 생각이 들었다.


## screenshot

<img width="598" alt="Screen Shot 2020-09-17 at 5 05 32 PM" src="https://user-images.githubusercontent.com/35520314/93438698-9f8b9100-f908-11ea-8ccf-afd6e226edfa.png">

