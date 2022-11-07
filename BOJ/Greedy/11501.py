"""
11501번 주식

1.  일반적으로 미래를 아는 사람이 주식을 할 때의 행동과 동일하게 행동하면 된다.
    즉, 고점을 찾고 그 전까지 매수했다가 고점에 매도, 이후에도 동일하게 고점 탐색 -> 구간 매수 -> 고점 매도를 반복하면 된다.
"""

import sys

T = int(input())

for _ in range(T):
    day = int(input())
    daily = list(map(int, sys.stdin.readline().split()))

    totalProfit = 0
    currentDate = 0

    maxPrice = max(daily)
    maxDate = daily.index(maxPrice)

    while True:
        if maxDate != 0:
            totalProfit = (
                totalProfit
                + maxPrice * (maxDate - currentDate)
                - sum(daily[currentDate:maxDate])
            )
            currentDate = maxDate + 1

            if currentDate == day:
                break

            maxPrice = max(daily[currentDate:])
            maxDate = daily[currentDate:].index(maxPrice) + currentDate
        else:
            break

    print(totalProfit)
