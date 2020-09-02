## 문제
- ⚠️ 스택 Lv2. 주식가격
- 언어 : Ptyhon 3
- https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3


## 풀이
- 정답 리스트에 0을 세팅해놓고 가격이 떨어지지 않으면 1씩 추가한다.
- i값이 i+1 값보다 커지는 경우는 가격이 떨어진 것이기 때문에 break
- answer 리스트에 cnt 한 값을 지정해준다.

## 코드

[ 정답 코드 ]
```
def solution(prices):
    answer = [0]*len(prices)
    
    for i in range(0,len(prices)-1):
        cnt=0
        for j in range(i+1,len(prices)):
            cnt +=1
            if prices[i] > prices[j]:
                break
        answer[i] = cnt
    
            
    return answer
```

## 보완점

append가 직접 값을 부여하는 것보다 효율성이 훨씬 많이 떨어지는 것 같다. <br>
처음에는 값을 pop해서 이전 값과 비교하고, 남은 값의 length를 확인하는 것으로 생각했는데 다른 테스트 코드를 통과하지는 못했다.


[ 🆇 시도한 코드 ]
```
def solution(prices):
    answer = [0]*len(prices)
    stack = []
    
    for i in range(0,len(prices)):
        a = prices.pop()
        slength = len(stack)
        if slength==0:
            stack.append(a)         
        elif a > stack[-1]:
            answer[i] = slength-1
            stack.append(a)
        else:
            answer[i] = slength
            stack.append(a)
    
    answer.reverse()
    return answer
```
👉첫 번째 테스트케이스 외에 맞추지 못함. 효율성도 0


## screenshot
<img width="598" alt="스크린샷 2020-09-02 오후 3 10 04" src="https://user-images.githubusercontent.com/35520314/91941294-f5bada80-ed33-11ea-87ec-feb2f7298e6f.png">


