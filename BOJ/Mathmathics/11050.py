"""
11050번 이항 계수 1

1.  이항 계수?
    (a+b)^n 꼴의 다항식을 전개했을 때, (a^r)(b^(n-r))의 계수를 의미 (0<=r<=n)
    (n) 로 나타나며, 조합과 동일한 의미로 nCr과 같다.
    (r)

2.  조합
    n개 원소에서 r개의 원소를 선택하는 경우의 수
    nCr = nPr/r! = n!/r!(n-r)!
"""

from math import factorial


N, K = map(int, input().split())

combination = factorial(N) // (factorial(K) * factorial((N - K)))

print(combination)
