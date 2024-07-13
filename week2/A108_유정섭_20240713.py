# https://www.acmicpc.net/problem/3062

for i in range(int(input())):
    print("YES" if ((r := (int(x := input())) + int(x[::-1])) == int(str(r)[::-1])) else "NO")
