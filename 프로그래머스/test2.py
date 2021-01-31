def solution(N, target):
    
    num_list = list({int(i*str(N))} for i in range(1,9))
    
    for i, number in enumerate(num_list, start = 1):
        for j in range(i):
            for x in num_list[j]:
                for y in num_list[i-j-1]:
                    num_list[i].add(x+y)
                    num_list[i].add(x-y)
                    num_list[i].add(x*y)
                    if y != 0:
                        num_list[i].add(x//y)
        if target in num_list[i]:
            return i+1
    
    return -1

if __name__ == '__main__':
    N = 2
    target = 11
    result = solution(N, target)
    print(result)