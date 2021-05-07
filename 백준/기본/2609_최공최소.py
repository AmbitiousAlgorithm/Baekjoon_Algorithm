import sys
import math

a, b = (map(int, sys.stdin.readline().split()))

divisor = math.gcd(a,b)
lcm = a * b // divisor

print(divisor)
print(lcm)
