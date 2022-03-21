"""
1463번 1로 만들기

1.  가장 처음 핵심 논리의 점화식을 구성.
    min(
            operation(number - 1),
            operation(number // 2),
            operation(number // 3),
        ) + 1 부분에서 Top-Down 방식의 DP를 구성.
    
    이후, 기본 점화식으로만으로는 시간 초과 -> visited 메모이제이션 적용
    
2.  Top - Down 방식의 DP
    상기의 점화식으로 접근 시 재귀 깊이가 너무 깊어져  1백만 이상의 재귀를 수행. 제한에 걸리게 됨
    따라서 변형 점화식으로 접근하여 2와 3으로 나눈 결과값이 2와 3으로 나눈 나머지를 더해주는 방식으로 변형
    이 경우, 2와 3으로 나누어 떨어지지 않는 경우 1까지의 진행 중에 -1 연산을 해주는 횟수만큼 나머지가
    계상되어 더해지는 논리
    
3.  Bottom - Up 방식의 DP
    operation은 총 3가지로,
    1) -1, 2) //2, 3) //3의 경우가 있는데 for문을 돌면서
    각 case를 동작시키는 if문을 거치면서 3가지 중 가장 작은 경우를 택해 저장해 놓고
    number까지 만들어 간다.

"""

import sys

visitedBU = [0 for i in range(pow(10, 7))]
visited = {1: 0, 2: 1}


def operation_TD(number):
    if number in visited:
        return visited[number]

    result = (
        min(
            operation_TD(number // 2) + number % 2,
            operation_TD(number // 3) + number % 3,
        )
        + 1
    )

    visited[number] = result
    return visited[number]


def operation_BU(number):
    for i in range(2, number + 1):
        visitedBU[i] = visitedBU[i - 1] + 1
        if i % 3 == 0:
            visitedBU[i] = min(visitedBU[i], visitedBU[i // 3] + 1)
        if i % 2 == 0:
            visitedBU[i] = min(visitedBU[i], visitedBU[i // 2] + 1)

    return visitedBU[number]


N = int(input())

print(operation_TD(N))
# print(operation_BU(N))
