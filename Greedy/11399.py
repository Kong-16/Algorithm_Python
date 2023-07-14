import sys

input = sys.stdin.readline

N = int(input())

time = list(map(int, input().split()))

time.sort()

acc = 0

for i in range(N):
    acc += time[i]
    time[i] = acc

print(sum(time))
