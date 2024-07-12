# https://www.acmicpc.net/problem/3135

current, target = map(int, input().split(" "))
arr = []
for _ in range(int(input())):
    arr.append(int(input()))
print(min(abs(target - current), 1 + abs(target - min(arr, key=lambda x: abs(target - x)))))
