"""
11047번 동전 0

1.  이 문제에서는 주어진 동전들로 원하는 금액을 최소 개수의 동전으로 만들어야 한다.
    그리디 알고리즘의 두 가지 조건
    1)  탐욕 선택 조건 : 앞의 행위가 뒤의 행위에 영향을 미치지 않음(현재 최선)
    2)  최적 부분 구조 조건 : 어떤 문제에 대한 최적해가 부분 문제에 대해서도 최적해
    이 만족되어야 한다.
    
2.  남은 금액 중 현재 고를 수 있는 남은 금액보다 작은 가장 큰 동전을 골라 줄이는 것은
    이후 남은 금액에서 동전을 고르는 것에 영향을 미치지 않으므로 1)은 만족된다.
    또한, 주어지는 동전들은 서로 배수관계에 있으므로 고를 수 있는 가장 큰 금액의 동전을 고르는 것이
    가장 적은 개수의 동전을 만들 수 있는 최적해이며 이것은 부분적인 금액에도 동일하므로
    2)도 만족된다. 따라서 그리디 알고리즘을 적용할 수 있다.
    
3.  추가적으로, 더 간단하게 논리를 전개해 보면
    가장 큰 동전 단위로 남은 금액을 나눴을 때 몫이 있다면 그것이 그 동전의 필요 갯수이다.
    또한 그 나머지는 해당 동전을 고를 수 있는 최대로 고르고 남은 금액이 될 것이므로,
    동전 리스트의 역순으로 남은 금액을 나누고 나머지로 계상하는 것을 반복하면 동일하게 구할 수 있다.
"""

import sys

N, K = map(int, sys.stdin.readline().split())

coins = [int(sys.stdin.readline()) for _ in range(N)]

remain = K
count = 0

while remain > 0:
    pick = 0
    for i, v in enumerate(coins):
        if v == remain:
            pick = coins[i]
            break
        elif v > remain:
            pick = coins[i - 1]
            break
    if pick == 0:
        pick = coins[-1]

    count += 1
    remain = remain - pick

print(count)
