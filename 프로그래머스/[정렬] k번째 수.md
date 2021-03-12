## 문제
- ⚠️ k번째 수
- 언어 : Ptyhon 3
- https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3


## 풀이
- commands를 순회하면서 len이 3으로 정해져있으니, i,j,k 변수에 값을 할당한다.
- array를 i-1:j 만큼 자르고 정렬한 뒤 k-1째 값을 answer에 넣으면 끝.

## 코드

[ 정답 코드 ]
```
def solution(array, commands):
    answer = []
    
    for command in commands:
        i,j,k = command
        sort_num = sorted(array[i-1:j])[k-1]
        answer.append(sort_num)
    return answer
```

## 보완점

본 정렬문제는 구현보다 코드를 어떻게 하면 python 스럽게 만들 수 있는지를 공부할 수 있는 문제같다.
참고할만한 코드를 갖고왔는데, lambda를 써서 특정 기준으로 정렬하는 방식을 사용했다.

list.sort(key = lambda x : x[-1])

list1 = ['1', '100', '33']
list2 = list(map(int, list1))

commands를 lambda를 써서 sorted(array[i-1:j])[k-1] 대로 정렬한 뒤 list로 바로 리턴해줬다.

🅇 참고할만한 코드
```
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
```


## screenshot

<img width="587" alt="스크린샷 2021-03-11 오후 5 27 51" src="https://user-images.githubusercontent.com/35520314/110758945-6c5f0480-8290-11eb-8f72-245c9586edd5.png">



