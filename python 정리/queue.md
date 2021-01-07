# 큐(Queue)

stack이 LIFO라면, 큐는 FIFO이다. FIFO(선입선출)는 가장 먼저 들어온 것이 가장 먼저 삭제되는 구조로, python에서는 queue와 deque가 있다.


1️⃣ Queue(큐)

 python의 queue 모듈은 여러 쓰레드가 동시에 큐를 사용해도 문제 없게끔 '동기화' 과정을 거치기 때문에 deque보다 많이 느리다.

 ```
from queue import Queue

q = Queue() # 생성하기
q.put(1) # 데이터 넣기
q.get() # 큐에서 데이터 제거하면서 반환
q.qsize() # 원소 수 반환

```

👉 우선순위 큐

FIFO 순서가 아니라 데이터 자체에 우선순위 정보가 있는 경우. (순위, 값) 인 튜플로 저장되며 순위가 높은 값(숫자가 낮은)부터 나온다.

| 메소드 | 역할 |
|---|---|
empty() | 큐가 비어있는지 검사
put_nowait(item) | item을 큐에 넣음(블로킹 없이 예외처리할 수 있도록 결과 반환)
get_nowait() | 가장 작은 원소를 pop
qsize() | 데이터 수 반환
queue | 현재 큐에 들어있는 데이터 반환
<br>

2️⃣ Deque(덱)

스택과 큐가 합쳐진 개념으로, 데이터 삽입(enqueue)와 삭제(dequeue)가 가능하다. 큐 모듈보다 훨씬 빠르다는 장점이 있다.

| 메소드 | 역할 |
|---|---|
append() | 원소 삽입
popleft() | 맨 앞(가장 처음들어온) 원소 pop
queue[0] | 맨 앞 원소 확인 가능
len() | python 그대로 원소 수 알아내기
clear() | 큐 비우기

<br>
<br>

참고 : https://han-py.tistory.com/29


e