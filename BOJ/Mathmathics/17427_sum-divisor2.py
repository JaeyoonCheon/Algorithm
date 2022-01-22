from functools import reduce
from math import sqrt

"""
1부터 N-1까지의 모든 수의 약수를 일일히 구해 결과 구함
def sumDivisor(N):
    f = [0]
    for i in range(1, N + 1):
        sum = 0
        for j in range(1, int(N / 2) + 1):
            if i % j == 0:
                sum += j
        if j < i:
            sum += i
        f.append(sum)

    return f


def func(x, y):
    return x + y


def sumF(f):
    total = reduce(func, f)
    print(total)


f = sumDivisor(int(input()))
total = reduce(func, f)
print(total)

"""

"""
위와 반대로, N이하 k를 약수로 갖는 수의 갯수 = N이하 k의 배수
라고 간주하여 풀이
N까지의 f(N)들에서 1~N 사이의 k가 포함되는 갯수는 N/k번
따라서, 1~N의 k각각에 N*k를 더하여 합산
"""


def counting(N):
    total = 0

    for i in range(1, N + 1):
        total += i * int(N / i)

    return total


print(counting(int(input())))
