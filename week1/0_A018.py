# https://www.acmicpc.net/problem/1026

# 정답이지만 잘못된 방법

# N = int(input())
# A = sorted([int(x) for x in input().split()])
# B = sorted([int(x) for x in input().split()])[::-1]

# print(sum([A[i] * B[i] for i in range(N)]))

# 맛는 방법 - B에 나오는 값들을 RANK 해야함.

N = int(input())
A = sorted([int(x) for x in input().split()])
B = [int(x) for x in input().split()]  # Sort 할 수 없음.
new_arr = [0] * len(B)
for idx, t in enumerate(sorted([f"{x}_{idx}" for idx, x, in enumerate(B)], key=lambda x: int(x.split("_")[0]))):
    new_arr[int(t.split("_")[1])] = sorted(A, reverse=True)[idx]
# print(new_arr)
print(sum([new_arr[i] * B[i] for i in range(N)]))
