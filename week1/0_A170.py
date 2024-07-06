# https://school.programmers.co.kr/learn/courses/30/lessons/82612


def solution(price, money, count):
    return max(0, sum([i * price for i in range(1, count + 1)]) - money)
