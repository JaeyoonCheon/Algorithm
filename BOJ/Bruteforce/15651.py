"""
15651번 N과 M (3)

1. 재귀 백트래킹 이용
스택에 수열을 저장하고 원래대로 되돌려 놓는 방식으로 가능한 모든 경우의 수를 탐색

2. 15649번에서 중복을 체크하는 조건문을 제거
"""


def getSequence(visited, N, M):
    if M == 0:
        for i in visited:
            print(f"{i} ", end="")
        print("")
        return
    for i in range(1, N + 1):
        visited.append(i)
        getSequence(visited, N, M - 1)
        visited.pop()


N, M = map(int, input().split())

visited = []

getSequence(visited, N, M)
