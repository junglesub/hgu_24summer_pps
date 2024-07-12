# https://www.acmicpc.net/problem/2480

print([10000, 1000, 0][(l := len(s := set(i := sorted(map(int, input().split(" ")), reverse=True))) - 1)] + max(map(lambda x: (x, i.count(x)), s), key=lambda x: (x[1], x[0]))[0] * [1000, 100, 100][l])
