# https://school.programmers.co.kr/learn/courses/30/lessons/133499

import re


def solution(babbling):
    noWords = ["aya", "ye", "woo", "ma"]
    cnt = 0

    for word in babbling:
        # 두번 연속 반복되는 단어가 있는지 확인
        if [noWord for noWord in noWords if noWord * 2 in word]:
            continue
        cnt += 1 if len(re.compile("|".join(map(re.escape, noWords))).sub("", word)) == 0 else 0
    return cnt

    # 포기.. 80점..
    # return len(set([""] + [word if len(re.compile("|".join(map(re.escape, [aw for aw in noWords if aw * 2 not in word and aw in word]))).sub("", word)) == 0 else "" for word in babbling])) - 1


print(solution(["yemawooyemawoowooye"]))
print(solution(["aya", "yee", "u", "maa", "yeyeye"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
