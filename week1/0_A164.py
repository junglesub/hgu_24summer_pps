# https://school.programmers.co.kr/learn/courses/30/lessons/142086


def solution(s):
    return [w - idx if (w := s[::-1].find(letter, idx + 1)) > -1 else -1 for idx, letter in enumerate(s[::-1])][::-1]
