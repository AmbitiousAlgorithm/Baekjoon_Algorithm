## 문제
- ⚠️ flag OR for-else
- 언어 : Ptyhon 3
- https://programmers.co.kr/learn/courses/4008/lessons/66568


## 풀이
- input 값 받아서 test 배열에 저장하고 첫 번째 값 pop해서 큐에 넣기
- 큐 값과 test배열 값을 각각 pop해서 곱하고, 그 값을 다시 큐에 넣는다.
- 만약 제곱수 조건이 충족되면 flag를 바꾼다.
- flag에 따라 멘트를 다르게 출력

## 코드

[ 정답 코드 ]
```
import math
from collections import deque

test = []
flag = 0
queue = deque()

for _ in range(5):
    inp = int(input())
    test.append(inp)
queue.append(test.pop(0))

while test:
    num = queue.popleft() * test.pop(0)
    queue.append(num)
    sqrt = math.sqrt(num)
    if sqrt == int(sqrt):
        flag = 1

if flag == 1:
    print("found")
else:
    print("not found")
    



```

## 보완점

처음에는 5개로 명시가 되어있으니까 a,b,c,d,e를 하나씩 input을 받았는데, for문으로 돌려서 input을 받아
test 배열에 넣는 방식을 스터디 내용을 보고 참고해서 변경했다. numbers = [int(input()) for _ in range(5)] 이런 방식을 생활화하자!
그리고 for문으로 돌았었는데, index에러 문제도 있고 무엇보다 이전에 곱한 값에서 새로 곱한다는 것을 간과하고 있었다.

1) 제곱수를 구하는 방법
math 모듈에서 math.sqrt하는 방법이 있고,
num ** 0.5를 해서 비교하는 방법도 있다.
2) input을 제대로 받아오기
numbers = [int(input()) for _ in range(5)]
3) 이전에 곱한 값에 다시 곱하기가 관건이었던 것 같다.
multiplied *= number 변수를 하나 세팅해서 하는 방법이 간단하고 큐를 쓸 필요가 없다. 
스터디에서 큐를 하다보니 자꾸 큐를 쓰게끔 생각하게 되는 것 같다.


💡 참고 코드 : 파이썬스럽게 푸는 법!

for 문 돌아서 맞으면 
else면 

```
import math

numbers = [int(input()) for _ in range(5)]
multiplied = 1
for number in numbers:
    multiplied *= number
    if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
        print('found')
        break
else:
    print('not found')
```

## screenshot

<img width="584" alt="스크린샷 2021-01-01 오후 10 46 50" src="https://user-images.githubusercontent.com/35520314/103439799-77d7f300-4c83-11eb-825c-7951fc49a85b.png">



