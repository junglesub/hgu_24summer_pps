# https://www.acmicpc.net/problem/1267

import math

input()
x = list(map(int, input().split(" ")))
y = sum(map(lambda e: math.ceil((e + 1) / 30) * 10, x))
m = sum(map(lambda e: math.ceil((e + 1) / 60) * 15, x))
print(f"{'M' if m < y else 'Y' if y < m else 'Y M'} {min(y, m)}")
