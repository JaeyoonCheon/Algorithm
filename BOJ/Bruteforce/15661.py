"""
15661번 링크와 스타트

* 중요! 14889번 스타트와 링크와는 다르게 팀 인원의 제한이 1명이상이면 되는 조건으로 변경

1. N명 중 M명을 중복 없이 뽑는 모든 경우를 고려(M>=1)
2. 해당하는 경우 마다 팀 별 점수의 합계의 차를 저장
2-1. 점수 계산 시 같은 팀에서 2명을 골라 점수를 추가하는 모든 경우를 고려
3. min값이 가장 낮은 경우를 출력

*   1. 전체에서 반을 고르는 모든 경우
    2. 점수 계산 시 같은 팀에서 2명을 고르는 모든 경우 (1명일 경우 0)
    이렇게 순열을 계산해야할 필요가 있다.
"""


def calculatePower(N, power, start, link):
    startSum = 0
    linkSum = 0
    if len(start) > 1:
        for i in range(int(len(start) - 1)):
            for j in range(i + 1, len(start)):
                startSum += power[start[i]][start[j]] + power[start[j]][start[i]]
    else:
        startSum = 0

    if len(link) > 1:
        for i in range(int(len(link) - 1)):
            for j in range(i + 1, len(link)):
                linkSum += power[link[i]][link[j]] + power[link[j]][link[i]]
    else:
        linkSum = 0

    diff = abs(startSum - linkSum)
    return diff


def findMinDiff(N, power, start, link):
    global min
    next = False
    for i in range(N):
        if i in start:
            continue
        for j in start:
            if i < j:
                next = True
        if next == True:
            next = False
            continue
        start.append(i)

        for item in range(N):
            if item not in start:
                link.append(item)
        diff = calculatePower(N, power, start, link)
        if min > diff:
            min = diff
        link.clear()

        findMinDiff(N, power, start, link)
        start.pop()


min = 10000

N = int(input())

power = []
for _ in range(N):
    power.append(list(map(int, input().split())))


start = []
link = []

findMinDiff(N, power, start, link)
print(min)
