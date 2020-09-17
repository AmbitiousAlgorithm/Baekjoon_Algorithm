## 문제
- ⚠️ 해시 Lv2. 전화번호부 목록
- 언어 : Ptyhon 3
- 


## 풀이
- 

## 코드

[ 정답 코드 ]
```

```

## 보완점

[ 🆇 시도한 코드 ]
```
import re

def solution(phone_book):
    answer = True
    
    # 리스트 -> 딕셔너리
    phone_book= dict(zip(range(len(phone_book)), phone_book))
    
    # 일부 일치하는 값이 있으면 false
    for k in phone_book.keys():
        for v in phone_book.values():
            if re.search("^"+phone_book[k],v) and phone_book[k]!=v:
                answer = False
        
            
    return answer

```
👉 테스트 케이스는 다 맞췄으나, 이중 for문으로 효율성 체크에서 시간초과로 실패.


## screenshot



