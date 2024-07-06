# https://school.programmers.co.kr/learn/courses/30/lessons/131705

from itertools import combinations


def solution(number):
    return sum([1 if sum(combi) == 0 else 0 for combi in combinations(number, 3)])
