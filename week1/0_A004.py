# https://school.programmers.co.kr/learn/courses/30/lessons/12910


def solution(arr, divisor):
    return x if len(x := sorted([x for x in arr if x % divisor == 0])) > 0 else [-1]
