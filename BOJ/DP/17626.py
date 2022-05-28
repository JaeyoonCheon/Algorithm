"""
17626번 Four Squares

1.  주어진 수를 1개 이상의 제곱수로 분해하여 최소의 제곱수의 합으로 이루어지도록 만드는 문제.

2.  DP bottom-up 방식으로 접근하여 어떤 수 K에 대해 1부터 root(K)까지의 수의 제곱 i를 K에서 뺀 값을
    제곱수로 만들 수 있는 최소 개수 +1인 DP[K-i]과 현재까지 K를 제곱수로 만들 수 있는 최소 개수가 저장된 
    DP[K]와 비교해 더 작은 수로 DP[K]를 갱신시켜 올라가면 가장 작은 경우의 수를 구할 수 있다.
"""

from math import floor


N = int(input())

DP = [50001] * 50001
DP[0], DP[1] = 0, 1


def findSquare(number):
    root = floor(number ** 0.5)

    for i in range(1, root + 1):
        DP[number] = min(DP[number - i ** 2] + 1, DP[number])


for i in range(2, N + 1):
    findSquare(i)

print(DP[N])
