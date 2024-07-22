# https://school.programmers.co.kr/learn/courses/30/lessons/178871?language=python3


def solution(players, callings):
    store = {}
    for idx, player in enumerate(players):
        store[player] = idx
    for call in callings:
        idx = store[call]
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
        store[players[idx]] = idx
        store[players[idx - 1]] = idx - 1
    return players


print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))
