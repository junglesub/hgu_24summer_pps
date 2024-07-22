# https://school.programmers.co.kr/learn/courses/30/lessons/138477


def solution(k, score):
    answer = []
    score_a = []

    for s in score:
        score_a.append(s)
        score_a = list(sorted(score_a, reverse=True))[:k]
        answer.append(score_a[-1])
    return answer


print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
