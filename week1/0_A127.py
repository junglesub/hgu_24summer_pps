# https://www.acmicpc.net/problem/1934
# https://mathbang.net/204#gsc.tab=0

import math

for _ in range(int(input())):
    i, j = map(int, input().split(" "))
    print(math.lcm(i, j))
    # ans = 1

    # keepGoing = True
    # while keepGoing:
    #     # 최소 공배수 구하기
    #     keepGoing = False
    #     for d in range(2, min(i, j)):
    #         if i % d == 0 and j % d == 0:
    #             i = int(i / d)
    #             j = int(j / d)
    #             ans *= d
    #             keepGoing = True
    #             break
    # print(ans * i * j)
