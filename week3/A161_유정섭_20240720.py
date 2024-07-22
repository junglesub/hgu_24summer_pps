# https://school.programmers.co.kr/learn/courses/30/lessons/160586


def solution(keymaps, targets):
    answer = []
    for target in targets:
        result = 0
        for c in target:
            works = False
            minMap = 999999
            for keymap in keymaps:
                if c in keymap:
                    minMap = min(minMap, keymap.index(c) + 1)
                    works = True
            result += minMap
            if not works:
                result = -1
                break
        answer.append(result)

    return answer


print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))
print(solution(["AA"], ["B"]))
