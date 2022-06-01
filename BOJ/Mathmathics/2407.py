"""
2407번 조합

조합 : nCr / n개의 수 중 r개를 뽑는 경우의 수
    nCr = n! / (n-r)!r!으로 구할 수 있다.
    순열 nPr에서 r개를 뽑아 순서를 나열하는 r!을 없애주는 것이므로
    nCr = nPr / r!와도 같다.
    nCr = n-1Cr + n-1Cr-1과도 같다.
    
1.  파이썬 math의 factorial 모듈로 풀이
    이 과정 중 나누는 중 정수를 남기도록 만들어야 부동소수점 오류를 피하도록 가능할 것으로 보임
    
2.  nCr = n-1Cr + n-1Cr-1 공식을 사용한 DP
    위의 식으로 nCr까지의 수를 만들어 갈 수 있는 점화식을 가지므로, DP를 사용해 수를 만들 수 있다.
"""

from math import factorial


N, M = map(int, input().split())


def useFactorialCombination():
    print(factorial(N) // (factorial(N - M) * factorial(M)))


def DPCombination():
    DP = [[], [1, 1]]

    for n in range(2, N + 1):
        """nC0 == 1"""
        temp = [1]
        for r in range(1, n):
            temp.append(DP[n - 1][r - 1] + DP[n - 1][r])
        temp.append(1)

        DP.append(temp)

    print(DP[N][M])


DPCombination()
