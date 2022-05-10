"""
1003번 피보니치 함수

1.  피보나치 응용

2.  0, 1을 반환할 경우를 따로 분리해서 반환
    0.25초 제한이므로 메모이제이션 적용
"""

cache = [0] * 42


def fibonacci(n):
    if cache[n]:
        return cache[n]
    if n == 0:
        return [1, 0]
    elif n == 1:
        return [0, 1]
    else:
        f1 = fibonacci(n - 1)
        f2 = fibonacci(n - 2)
        cache[n] = [f1[0] + f2[0], f1[1] + f2[1]]
        return cache[n]


T = int(input())

for _ in range(T):
    result = fibonacci(int(input()))
    print(f"{result[0]} {result[1]}")
