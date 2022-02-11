"""
15652번 N과 M (4)

1. 중복 조건 제거
2. 이전 선택값보다 작은 값일 경우 건너뛰는 조건
"""


def getSequence(visited, N, M):
    if M == 0:
        for i in visited:
            print(f"{i} ", end="")
        print("")
        return
    for i in range(1, N + 1):
        flag = False
        for j in visited:
            if i < j:
                flag = True
        if flag == True:
            continue
        visited.append(i)
        getSequence(visited, N, M - 1)
        visited.pop()


N, M = map(int, input().split())

visited = []

getSequence(visited, N, M)
