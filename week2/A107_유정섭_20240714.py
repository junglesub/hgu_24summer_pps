# https://www.acmicpc.net/problem/1292

ans = []
s, f = map(int, input().split(" "))
for i in range(1, f + 1):
    ans += [i] * i
print(sum(ans[s - 1 : f]))
