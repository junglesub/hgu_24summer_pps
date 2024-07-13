# https://www.acmicpc.net/problem/2010

import sys

input = sys.stdin.readline

ans = 0
for i in range(int(input())):
    ans += int(input()) - 1
print(ans + 1)
