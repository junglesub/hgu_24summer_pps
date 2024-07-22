# https://www.acmicpc.net/problem/1966

n = int(input())

for _ in range(n):
    docN, k = map(int, input().split(" "))
    priorty = list(map(int, input().split(" ")))

    cnt = 0
    while True:
        if priorty[0] < max(priorty):
            priorty = priorty[1:] + [priorty[0]]
            if k == 0:
                k = len(priorty) - 1
            else:
                k -= 1
            continue
        cnt += 1
        priorty = priorty[1:]
        if k == 0:
            break
        k -= 1

    print(cnt)
