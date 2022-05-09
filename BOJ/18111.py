"""
18111번 마인크래프트

1.  N*M 크기의 공간에 256 높이 이하로 쌓여져 있는 블록들을 B개의 여유 블록들을 가지고
    더하거나 빼 평평하게 만드는 문제.

2.  가장 처음에는 완전탐색으로 0~256 높이 모두에 대해 해당 높이가 될 경우의 연산시간을 계산
    블록을 빼는 경우를 우선적으로 고려하여 인벤토리에 먼저 저장하고, 이후 블록을 추가하여
    블록 가감에 여유 블록이 없어 중도 종료되는 경우가 없도록 작성
    이렇게 풀이할 경우, 시간 복잡도가 O(N^3)이 되어 시간 초과가 발생
    
3.  flat2()는 위의 풀이와 약간 다르게 검사하려는 층계보다 높은 블록의 개수와 낮은 블록의 개수를
    먼저 구하고 검사 범위를 총합계를 이용하여 좁혀 시간을 줄였다.

4.  총 블록 개수/층 마다 필요한 블록 개수/한 층에 모두 채우기 위한 개수를 미리 계산해 놓는다면
    loop 안에서 이중 loop를 사용할 필요 없이 O(N)시간 내에 풀이 가능할 것으로 생각됨
"""

N, M, B = map(int, input().split())
place = [list(map(int, input().split())) for _ in range(N)]


def flat():
    unit = N * M
    currentSum = 0
    minTime = 500 * 500 * 256 + 1
    maxHeight = -1

    for i in place:
        currentSum += sum(i)

    for layer in range(256):
        accuTime = 0
        inventory = B
        isPossible = True

        # 먼저 목표 높이보다 높은 블록들을 제거 후 인벤토리에 추가해야 함
        for i in range(N):
            for j in range(M):
                if layer < place[i][j]:
                    accuTime += 2 * (place[i][j] - layer)
                    inventory += place[i][j] - layer

        # 원래 가지고 있던 블록 + 캐낸 블록으로 목표 높이보다 낮은 블록들을 메꿈
        for i in range(N):
            for j in range(M):
                if layer > place[i][j]:
                    accuTime += layer - place[i][j]
                    inventory -= layer - place[i][j]
                    if inventory < 0:
                        isPossible = False

        if isPossible:
            if minTime > accuTime:
                minTime = accuTime
                maxHeight = layer
            elif minTime == accuTime:
                if maxHeight < layer:
                    maxHeight = layer

    return minTime, maxHeight


def flat2():
    minTime = 500 * 500 * 256 + 1
    maxHeight = -1
    unit = N * M
    currentSum = 0
    for i in place:
        currentSum += sum(i)
    maxLayer = (currentSum + B) // unit

    for layer in range(maxLayer + 1):
        accuTime = 0
        isPossible = True
        upperLayer = 0
        lowerLayer = 0

        for i in range(N):
            for j in range(M):
                if layer < place[i][j]:
                    upperLayer += place[i][j] - layer
                elif layer > place[i][j]:
                    lowerLayer += layer - place[i][j]

        if upperLayer - lowerLayer + B < 0:
            isPossible = False
        else:
            accuTime = 2 * upperLayer + lowerLayer

        if isPossible:
            if minTime > accuTime:
                minTime = accuTime
                maxHeight = layer
            elif minTime == accuTime:
                if maxHeight < layer:
                    maxHeight = layer

    return minTime, maxHeight


minTime, maxHeight = flat2()

print(f"{minTime} {maxHeight}")
