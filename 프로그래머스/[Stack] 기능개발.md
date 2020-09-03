## 문제
- ⚠️ 스택 Lv2. 기능개발
- 언어 : Ptyhon 3
- https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3


## 풀이
- list,map,lambda를 사용하여 progresses에서 100씩을 빼고, speeds로 나누는 연산 수행
- 올림하기 위해 import math하고 ceil사용
- 첫 값과 비교해서 더 큰 값이 있다면 멈추고 길이를 answer에 입력
- 시작은 큰 값의 인덱스부터 시작
- 마지막은 전체 길이에서 key값을 빼서 answer에 더해서 +1을 해준다.

## 코드

[ 정답 코드 ]
```
import math
def solution(progresses, speeds):
    answer = []
    dev = list(map(lambda x,y: math.ceil((100-x)/y),progresses,speeds))
    key =0
    
    for j in range(len(dev)):
        if dev[key] < dev[j]:
            answer.append(len(dev[key:j]))
            key = j
    answer.append(len(progresses)-key)
    return answer
```

## 보완점
python 라이브러리들을 많이 사용하여 비교적 짧고 간단하게 코딩할 수 있었다.<br>
더 다양한 라이브러리들을 찾아서 활용하도록 노력할 것!
마지막 값이 조건을 만족하지 못했을 때 어떻게 처리할지를 빨리 생각하지 못했다.

## screenshot

<img width="598" alt="스크린샷 2020-09-03 오후 1 44 27" src="https://user-images.githubusercontent.com/35520314/92072374-121a4e00-edec-11ea-9703-84460d21824e.png">

![이름 없는 노트북-2](https://user-images.githubusercontent.com/35520314/92072430-32e2a380-edec-11ea-999b-e1c5c60f2629.jpg)