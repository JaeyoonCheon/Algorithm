"""
2775번 부녀회장이 될테야

1.  피보나치 삼각형과 유사한 아파트 합 계산 문제.
    인덱스만 혼동하지 않으면 쉽게 해결 가능
"""

T = int(input())

for _ in range(T):
    K = int(input())
    N = int(input())

    apart = [[i for i in range(N + 1)]]

    for i in range(1, K + 1):
        tempFloor = [0]
        for j in range(1, N + 1):
            house = sum(apart[i - 1][: j + 1])
            tempFloor.append(house)
        apart.append(tempFloor)

    print(apart[K][N])
