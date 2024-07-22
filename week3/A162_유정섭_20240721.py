# https://school.programmers.co.kr/learn/courses/30/lessons/159994


def solution(cards1, cards2, goal):
    answer = "Yes"
    for word in goal:
        if len(cards1) > 0 and cards1[0] == word:
            cards1 = cards1[1:]
            continue
        if len(cards2) > 0 and cards2[0] == word:
            cards2 = cards2[1:]
            continue
        answer = "No"
        break
    return answer
