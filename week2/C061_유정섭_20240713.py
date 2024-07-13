# https://www.acmicpc.net/problem/11478

# from itertools import combinations_with_replacement

# print(len(set(word[a : b + 1] for a, b in combinations_with_replacement(range(len(word)), 2))))


word = input()
print(len(set(word[a : b + 1] for (a, b) in ((i, j) for i in range(len(word)) for j in range(i, len(word))))))
