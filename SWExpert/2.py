"""

"""


def checkCell():
    count = 0

    for i in range(N):
        rowMax = max(mars[i])
        rowMaxIdx = mars[i].index(rowMax)

        isMaximum = True

        for j in range(N):
            if j == i:
                continue
            if mars[j][rowMaxIdx] > rowMax:
                isMaximum = False

        if isMaximum:
            count += 1

    return count


T = int(input())

for _ in range(T):
    N, M, Q = map(int, input().split())

    mars = []

    for i in range(N):
        mars.append(list(map(int, input().split())))

    totalCount = 0

    for _ in range(Q):
        R, C, X = map(int, input().split())
        mars[R - 1][C - 1] = X
        count = checkCell()
        totalCount += count

    print(totalCount)
