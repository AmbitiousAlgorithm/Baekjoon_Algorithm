# 예은언니 코드

def hanoi(n, A, B, C):
    if n is 1:
        print(A, C)
    else:
        hanoi(n-1,A, C, B)
        print(A, C)
        hanoi(n-1,B, A, C)
        
if __name__ == "__main__":
    plate = int(input())
    print(pow(2, plate)-1)
    hanoi(plate, '1', '2', '3')

