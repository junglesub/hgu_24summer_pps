# https://www.acmicpc.net/problem/9237

input()
print(max([x + idx + 1 for idx, x in enumerate(sorted(map(int, input().split(" ")), reverse=True))]) + 1)
