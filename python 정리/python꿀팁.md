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
