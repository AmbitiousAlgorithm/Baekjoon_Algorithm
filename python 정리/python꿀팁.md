<br>

# 🍯 python을 python스럽게 만드는 문법 정리


<br>

### 1) 원본유지 정렬 : sorted()

list.sort() : 원본 정렬
list.sorted() : 정렬된 새로운 리스트

<br>

### 2) 이중리스트 행열 뒤집기,리스트 합치기 : zip

```
mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
new_list = list(map(list, zip(*mylist)))

zip(list1,list2) 하면 각각 원소 인덱스에 해당하는 값들끼리 묶어줌.
dict(zip(list1,list2)) 하면 key : value 형태로 묶임
```

<br>

### 3) 타입 한꺼번에 변환하기 : map

map은 int,list,str,len 등 다양하게 활용 가능하다.

```
list1 = ['1', '100', '33']
list2 = list(map(int, list1))
```

<br>

### 4) 하나로 이어붙이기 : join

''을 기준으로 리스트 값을 다 이어붙여준다.
',' 이런 방식이라면 ,을 기준으로 붙여짐.

```
answer = ''.join(my_list)
```

<br>

### 5) 곱집합 만들기 : itertools.product 
두 스트링 'ABCD', 'xy' 의 곱집합은 Ax Ay Bx By Cx Cy Dx Dy 입니다.
경우의 수를 계산해줌.

```
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
itertools.product(iterable1, iterable2, iterable3)
```
<br>

### 6) 2차원 리스트를 1차원으로 : from_iterable
https://programmers.co.kr/learn/courses/4008/lessons/12738 -> 다양한 방식

```
import itertools
list(itertools.chain.from_iterable(my_list))
list(itertools.chain(*my_list)) // unpacking
```
<br>

### 7) 순열/조합 : itertools permutations, combinations

```
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
```

### 8) 가장 많이 나온 값 찾기: Collections Counter

```
answer = collections.Counter(my_list)
```

### 9) 이진탐색 : bisect
이진탐색은 오름차순으로 정렬된 리스트에서 특정한 값의 위치를 찾는 알고리즘으로, 검색 속도가 아주 빠름.

```
import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))
```

<br>

### 10) 파일 출력 : with ~ as

파일을 close 하지 않아도 됩니다: with - as 블록이 종료되면 파일이 자동으로 close 됩니다.
readlines가 EOF까지만 읽으므로, while 문 안에서 EOF를 체크할 필요가 없습니다.

⨳ with - as 구문은 파일 뿐만 아니라 socket이나 http 등에서도 사용할 수 있습니다.

```
with open('myfile.txt') as file:
  for line in file.readlines():
    print(line.strip().split('\t'))``

```
### 11) 클래스 인스턴스 출력 : __str__

```
class Coord(object):
    def __init__ (self, x, y):  // class 정의하고 
        self.x, self.y = x, y
    def __str__ (self):  // __str__로 형식 지정 가능
        return '({}, {})'.format(self.x, self.y)

point = Coord(1, 2)
```



<br>

** 그외에도 
- 매우 큰 값을 할당하는 float('inf')
- 몫(//)과 나머지(%)를 한 번에 반환해주는 *divmode(5,6) 
- 진법 변환에 사용되는 int(num, base)
- 문자열 정렬에 활용되는 문자열.ljust(문자열 길이), center(),rjust()
- 알파벳 import string , string.ascii_lowercase


1) 입력 순서 그대로 둔채 / 숫자 혹은 문자 조합의 정렬이라면 --> 스택  or greedy 
 :  뽑아 가면서 순회하기 -  스택

2) 입력 숫자/문자를 계속 업데이트 하면서 정렬해야하는 상황... -->  힙 자료구조 

3) 리스트 인덱스 앞에서 부터 순서대로 뽑아야 하는 상황이면 --> 큐 (deque 자료형태 만들고)

https://huidea.tistory.com/90


4) dx dy 등으로 좌표를 이동해서 순회하면서 이게 맞는 값인지 체크하는 문제 ---> 큐 
방문 리스트를 만드는 것이 좋다.



def main():
    p, n, h = map(int,input().split())
    customers = {}
    income = 0
    
    if n == 0 or h == 0:
        income = 0
    
    for _ in range(n):
        x, y = map(int,input().split())
        customers[x] = y
        
    # y 기준으로 y 기준으로 정렬하기
    sorted(customers.items(), key = lambda x:x[1])
    
    print(customers)
    # for pc in range(p


## 최대공약수와 최소공배수

- 유클리드 호제법: a를 b로 나눈 나머지와 b를 a%b와 나눈 나머지가 같다. log수준으로 빠르게 계산 가능

def gcd(a,b):
    return b if a%b == 0 else gcd(b, a%b)

약수 배수 관계일 때는 반환해주고, 나누어떨어지지 않는다면 gcd...로 단계를 줄여나가기.

## 소인수분해

def isPrime(N):
    for i in range(2, N):
        if N % i == 0: return False
    return True

중간 수까지만 체크하면 알 수 있음. 루트 N까지 나누어떨어지는게 있으면 소수가 아니고, 없으면 소수다.

```
def isPrime(N):
    i = 2
    while i*i <= N:
        if N%i == 0: return False
        i+=1
    return Trues
```

- 에라토스테네스의 체

아직 지워지지 않았다 = 배수를 지우는 것이기 때문에 소수다.
지워지지 않은 수를 prime 배열에 추가해주고, 하나씩 지우는 과정에서,
6같은 경우는 이미 2에서 지워졌기 때문에 3에서 지울 필요는 없고, 9부터 지우면 된다...그러므로 
num*num부터 지우면 된다. num만큼 건너뛰면서 체크했다고 체크.

=> 다 끝나면 소수 판별, prime에는 소수만 담김

nlogN

```
def isPrime(N):
    chk, prime = [False]*(N+1), []
    
    for num in range(2, N+1):
        if chk[num] == True:
            continue
        prime.append(num)
        for j in range(num*num, N+1, num):
            chk[j] = True
    return chk, prime
```


```
def isPrime(N):
    prime = [True]*(N+1)
    prime[0] = False
	prime[1] = False 

    for num in range(2, N+1):
        if not prime[num]: continue
        for mul in range(num*num, N+1, num):
            prime[mul] = False
    
    return [idx for idx, value enumerate(prime) if value]
```

## 분할 정복

- 하노이탑 : 자신보다 큰 판은 올라올 수 없고, 작은 판만 올릴 수 있다.

마지막 큰 판을 옮기려면 나머지가 모두 한 곳에 있어야 한다.
N개 중 N-1개를 기둥 2에 보내는 것이 우선이다.
N번째 기둥을 3번에 보내고...N-1기둥을 3번에 보내고....

F(N) = 2 * F(N-1) + 1 # N-1개를 2번 옮기고 마지막에 한 번 옮기면 된다.
F(1) = 1
....
재귀로

```
def hanoi(start, end, size):
    # 최저 조건문
    if size == 1: return print(start, end) # 사이즈가 한 개다. 출발~end까지 하나
    middle = 6-start-end

    hanoi(start, middle, size-1)  # start~중간기둥까지
    print(start, end)
    hanoi(middle, end, size-1) # 중간기둥~end까지 다시 끝

    #출발점과 도착점을 정하면 나머지 중간 기둥은 정해진다. 1 (2) 3 = 합은 항상 6
n = int(input())
print(2**n-1)
hanoi(1,3,n)

```

## sort 알고리즘

- 선택 정렬

리스트 내에서 최솟값을 찾아 앞으로 바꿔줌. 최솟값을 찾고 하나씩 값을 갱신하는 정렬

** 시간 복잡도
한 번 순회할때마다 O(N) N부터 1...까지니까 n(n+1)/2  => O(N^2)


- 버블 정렬

31287564 옆의 수를 비교해서, 앞에 있는 수가 크면 무조건 바꿔준다. 
13287564
12387564....
계속 2개씩 비교하면서 나아감. 최댓값은 어디에 있던 간에 한 번의 과정을 거치면 가장 끝점에 도달하게 됨. 이 한 과정을 하는데 N번의 바꾸는 연산을 하게 되고, 이 연산이 끝나면 최댓값이 끝. 
그 다음 최댓값...N-1번....N-2번...

** 시간복잡도
O(N^2)


- 퀵 정렬

31285764
key : 3(첫번째)
3 기준으로 작은 걸 왼쪽 큰걸 오른쪽! 
key : 1 
1,2,3 고정 8보다 작은 친구들을 다 왼쪽으로 두고... 이분탐색과 같다.
key 8일 때 5764 8
key 5일 때 4 5 76 8....

** 시간 복잡도
T(N) = 2T(N/2) + N
     = 2(2T(N/4)+ N/2) + N (N을 그저 N/2으로만 바꿨음.) 
     = 4T(N/4) + 2N
     = 8T(N/8) + 3N
     = ..... 한 개는 정렬할 필요없으니까 1이 될 때까지...
     = 2^k T(N/2^k) + KN
     이만큼의 연산만 하면 정렬이 된다.

Nlog2N 만 정렬하면 된다~~

퀵 소트는 역순으로 정렬된 경우가 최악의 경우 O(N^2)가 되는데, 이를 막기 위해 key를 중앙으로 잡아서 최적화한다. 이런 경우 경우에 따라 달라져서 unstable

- Merge 정렬(병합정렬)

리스트를 반으로 나누고, 또 나눈다. 각각 2개가 될 때 까지
앞에서부터 두 개를 정렬 3281 4576 , 32 81 45 67, 그리고 23, 18, 45, 67까지 됨.

2 pointer라는 개념으로 정렬한다.
2를 가리키는 인덱스 변수 a가 있고 1을 가지고 있는 인덱스 변수 b
각자 가리키고 있는 애들을 비교 -> 1이 더 작으니까, 1을 앞으로 두고 b를 한 칸 움직여서 8로 간다.
a = 2, b = 8이니까 a의 포인터를 움직인다....


** 시간 복잡도

정렬된 T(n/2)*2 + N번 
한 줄을 처리하는데 걸리는 시간은 무조건 O(N) 블럭블럭 합치는 시간이 N 번 걸리니까.
NlogN
배열을 미리 준비해놔야해서 메모리 할당이 많이 들음.


- Radix 정렬

메모리가 넘쳐서 수의 제한을 알고 있을 때 사용
최솟값 최댓값 배열을 미리 만들어서 값을 하나씩 count해준다. for문으로 반복해서 읽으면서 정렬하는 방법.
범위가 짧을 때 사용












