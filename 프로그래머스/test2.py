def solution(num, k):

    divisor = []

    for n in range(1, num):
        if num % n == 0:
            divisor.append(n)
    divisor.append(num)

    return divisor[k]

if __name__ == '__main__':
    result = solution(6,3)
    print(result)