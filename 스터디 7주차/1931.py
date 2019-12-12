N = int(input())
time = []

for i in range(N):
    start,end = map(int,input().split())
    time.append((start,end))

time.sort(key= lambda x:(x[1],x[0]))
# start end에는 각각 마지막 값이 들어가 있음.
endtime = count =0

for i in time:
    if i[0] >= endtime: #0보다 start:1이 크면
        endtime = i[1]  #endtime은 4가 됨.
        count += 1
        
      
print(count)