"""
14889번 스타트와 링크

1. N명 중 N/2명을 중복 없이 뽑는 모든 경우를 고려
2. 해당하는 경우 마다 팀 별 점수의 합계의 차를 저장
2-1. 점수 계산 시 같은 팀에서 2명을 골라 점수를 추가하는 모든 경우를 고려
3. min값이 가장 낮은 경우를 출력

*   1. 전체에서 반을 고르는 모든 경우
    2. 점수 계산 시 같은 팀에서 2명을 고르는 모든 경우
    이렇게 순열을 계산해야할 필요가 있다.
"""
def calculatePower(N, power, start, link):
    startSum = 0
    linkSum = 0
    for i in range(int((N/2)-1)):
        for j in range(i+1, int(N/2)):
            startSum += power[start[i]][start[j]] + power[start[j]][start[i]]
            linkSum += power[link[i]][link[j]] + power[link[j]][link[i]]
            
    diff = abs(startSum - linkSum)
    return diff

def findMinDiff(N, power, start, link):
    global min
    next = False
    # 1팀 2팀 리스트
    # 1팀에 N/2명이 포함될 때 까지 재귀로 한 명씩 포함
    # 1팀에 N/2명이 포함된 경우 나머지 N/2명을 2팀에 포함
    # 이후 각 팀의 점수를 계산하여 그 차를 기록
    # 백트래킹으로 모든 경우에 대해 연산
    if len(start) == N/2:
        for i in range(N):
            if i not in start:
                link.append(i)
        diff = calculatePower(N, power, start, link)
        if min > diff:
            min = diff
        link.clear()
    else:
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