from math import gcd
from functools import reduce


def solution(arrayA, arrayB):
    gcd()
    gcdA = reduce(gcd, arrayA)
    gcdB = reduce(gcd, arrayB)

    if gcdA > 1:
        for n in arrayB:
            if n % gcdA == 0:
                gcdA = 0
                break
    if gcdB > 1:
        for n in arrayA:
            if n % gcdB == 0:
                gcdB = 0
                break

    answer = max(gcdA, gcdB)
    return answer
