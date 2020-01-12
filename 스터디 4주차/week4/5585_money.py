money = 1000 - int(input())
change = [500,100,50,10,5,1]
cnt = 0

for i in change:
    while money - i >=0:  # money >= i 인거니까 i로 거스를 수 있는 것
        x = int(money / i)
        money = money - i*x
        cnt += x
        
        if money == 0:
            break
print(cnt)   

