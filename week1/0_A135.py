# https://www.acmicpc.net/problem/1302

l = []
for _ in range(int(input())):
    l.append(input())
print(max(map(lambda x: (x, l.count(x)), sorted(l)), key=lambda x: x[1])[0])
