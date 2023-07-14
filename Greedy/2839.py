import sys

input = sys.stdin.readline

N = int(input())

num = N
cnt = 0

cnt = num // 5
num = num % 5


while num <= N:
    if num % 3 != 0:
        num += 5
        cnt -= 1
    else:
        cnt += num // 3
        num = 0
        break


if num != 0:
    print(-1)

else:
    print(cnt)
