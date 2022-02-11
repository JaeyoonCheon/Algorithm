"""
15650번 N과 M(2)

1. 15649번 문제에서 현재 선택한 수가 이전에 선택했던 수 보다 작으면 가지치기 하는 조건을 추가
"""


def getSequence(visited, N, M):
    if M == 0:
        for i in visited:
            print(f"{i} ", end="")
        print("")
        return
    for i in range(1, N + 1):
        flag = False
        if i in visited:
            continue
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
