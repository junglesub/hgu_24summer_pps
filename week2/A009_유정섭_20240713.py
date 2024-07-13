# https://school.programmers.co.kr/learn/courses/30/lessons/12918


def solution(s):
    return ((l := len(s)) == 4 or l == 6) and s.isdigit()


solution("")
