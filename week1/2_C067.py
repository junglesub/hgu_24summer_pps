# https://www.acmicpc.net/problem/2798

from itertools import combinations

N, M = map(int, input().split(" "))
print(max(map(sum, combinations(map(int, input().split(" ")), 3)), key=lambda x: x if x <= M else -1))
