# https://school.programmers.co.kr/learn/courses/30/lessons/147355


def solution(t, p):
    return len([int(r) for x in range(len(t) - len(p) + 1) if int(r := t[x : x + len(p)]) <= int(p)])


print(solution("10203", "15"))
