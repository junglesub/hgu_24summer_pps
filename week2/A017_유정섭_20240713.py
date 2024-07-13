# https://www.acmicpc.net/problem/1475

import math

n = input().replace("6", "9")
cnts = list(map(lambda x: n.count(str(x)), range(0, 10)))
cnts[9] /= 2
print(math.ceil(max(list(cnts))))
