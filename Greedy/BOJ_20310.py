import sys

input = sys.stdin.readline

nums = [0, 0]

inp_str = list(input().strip())

zero = inp_str.count('0') // 2
one = len(inp_str) // 2 - zero

for _ in range(zero):
    inp_str = inp_str[::-1]
    inp_str.remove('0')
    inp_str = inp_str[::-1]

for _ in range(one):
    inp_str.remove('1')

print(''.join(inp_str))
