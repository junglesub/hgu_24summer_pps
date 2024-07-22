# https://school.programmers.co.kr/learn/courses/30/lessons/12906


def solution(arr):
    ans = [arr[0]]
    for x in arr[1:]:
        if ans[-1] != x:
            ans.append(x)
    return ans


print(solution([1, 1, 3, 3, 0, 1, 1]))
