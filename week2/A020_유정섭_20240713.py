# https://www.acmicpc.net/problem/2455

ans = [0]
for _ in range(4):
    o, i = map(int, input().split(" "))
    ans.append(ans[-1] + i - o)

print(max(ans))
