# https://www.acmicpc.net/problem/5585

x = int(input())

amt = 1000 - x
cnt = 0

while amt > 0:
    for c in [500, 100, 50, 10, 5, 1]:
        if amt >= c:
            amt -= c
            cnt += 1
            break
print(cnt)
