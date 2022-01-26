"""
1107 리모컨

첫 시도 - 원하는 채널에서 양방향으로 멀어지는 채널을 검사해 최단 거리의 채널을 찾으려는 시도
구현의 복잡함 + 2초 시간제한으로 넉넉한 점으로 인해 가능한 채널을 모두 비교하도록 새로 구현

두번쨰 시도 - 0~1000001 채널 구간에서 0~500000 사이의 원하는 채널과 가장 가까운 채널을 모두 검사
이 경우, 초기 채널이 100부터 시작한다는 점에 의해 여러 예외를 고려해주어야 TC에 걸리지 않음
"""


from imghdr import tests


def findClosest(N, M, fail):
    channel = list(N)
    button = []
    pos = []
    movedP, movedM = -1

    for i in range(len(channel), -1, -1):
        movedP, movedM = -1
        for j in range(6):
            moveP = int(channel[i]) + j
            moveM = int(channel[i]) - j
            if moveP not in fail:
                movedP = moveP
            if moveM not in fail:
                movedM = moveM
            if movedP or movedM != -1:
                break
        if movedP == -1:
            button.insert(movedM)
            break
        if movedM == -1:
            button.insert(moveP)
            break
        if movedP == movedM:
            button.insert(movedP)


def findCloestBrute(N, fail):
    maxDistance = abs(100 - N)
    maxChannel = 100
    for i in range(1000001):
        flag = 0
        check = list(str(i))
        for digit in check:
            if int(digit) in fail:
                flag = 1
                break
        if flag == 1:
            continue
        else:
            distance = abs(N - i)
            if distance < maxDistance:
                maxDistance = distance
                maxChannel = i
    return maxDistance, maxChannel


N = int(input())
M = int(input())

fail = []

if M != 0:
    fail = list(map(int, input().split()))

pressButton = 0
dist, channel = findCloestBrute(N, fail)
if channel != 100:
    if abs(N - 100) < dist + len(str(channel)):
        pressButton = abs(N - 100)
    else:
        pressButton = dist + len(str(channel))
else:
    pressButton = dist

print(pressButton)
