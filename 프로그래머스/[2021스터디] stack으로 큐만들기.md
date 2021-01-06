## 문제
- ⚠️ 최대 용량이 정해진 FIFO 큐 클래스
- 언어 : Ptyhon 3


## 풀이
- stack은 LIFO고 큐는 FIFO이다. stack 2개로 FIFO를 만들어야한다.
- 명령어는 input 값들을 받아서 명령어를 분리한다음, PUSH인 경우에만 값을 따로 받았다.

![알고리즘 연습장-30](https://user-images.githubusercontent.com/35520314/103782648-12b54080-507b-11eb-95ec-cb5a5e5429f7.jpg)

## 코드

[ 정답 코드 ]
```
class MyStack(object):
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)

class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        self.max_size = max_size

    def qsize(self):
        # 원소 수 리턴
        return self.stack1.size()
        pass

    def push(self, item):
        # 인자를 큐에 넣기, 큐가 찼으면 false
        if (self.qsize() == self.max_size):
            return False
        else:
            self.stack1.push(item)
            return True
        pass

    def pop(self):
        # 가장 처음 들어온 원소 제거 후 리턴, 비어있으면 Empty Exception 직접 만들어서 raise
        try:
            if self.stack1.size() == 0:
                raise emptyException
            
            # stack1을 뒤집어서 stack2에 넣는다.
            while self.stack1.size() > 0:
                item = self.stack1.pop()
                self.stack2.push(item)
            # stack2 pop 값 == 처음 들어온 값    
            first = self.stack2.pop()
            # stack1 에 다시 넣어준다.
            while self.stack2.size() >0:
                item = self.stack2.pop()
                self.stack1.push(item)
            
            return first
            
        except emptyException:
            return False
        
class emptyException(Exception):
    pass

n, max_size = map(int, input().strip().split(' '))
q = MyQueue(max_size)

for _ in range(n):
    inp = input()
    command = inp.split(' ')[0]
    if command == 'PUSH':
        X = inp.split(' ')[1]
        print(q.push(X))
    elif command == 'POP':
        print(q.pop())
    elif command == 'SIZE':
        print(q.qsize())

```

## 보완점

stack1에서 pop해와서 stack2에 정렬했으면, stack1이 비어있다는 것을 간과하였다.

🅇 실패한 코드
```
class MyStack(object):
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)

class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        self.max_size = max_size

    def qsize(self):
        # 원소 수 리턴
        return self.stack1.size()
        pass

    def push(self, item):
        # 인자를 큐에 넣기, 큐가 찼으면 false
        if (self.qsize() == self.max_size):
            return False
        else:
            self.stack1.push(item)
            return True
        pass

    def pop(self):
        # 가장 처음 들어온 원소 제거 후 리턴, 비어있으면 Empty Exception
        try:
            if self.stack1.size() == 0:
                raise BaseException
            if self.stack1.size() > 0:
                first = self.stack1.pop()
                self.stack2.push(first)
            
            return self.stack2.pop()
            
        except BaseException:
            return False
        pass
    
n, max_size = map(int, input().strip().split(' '))
q = MyQueue(max_size)

for _ in range(n):
    inp = input()
    command = inp.split(' ')[0]
    if command == 'PUSH':
        X = inp.split(' ')[1]
        print(q.push(X))
    elif command == 'POP':
        print(q.pop())
    elif command == 'SIZE':
        print(q.qsize())
```


## screenshot

<img width="584" alt="스크린샷 2021-01-01 오후 10 46 50" src="https://user-images.githubusercontent.com/35520314/103439799-77d7f300-4c83-11eb-825c-7951fc49a85b.png">



