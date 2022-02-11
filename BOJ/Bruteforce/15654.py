"""
15654번 N과 M (5)

1. 입력된 자연수 set을 정렬 저장
"""


def getSequence(dataset, visited, N, M):
    if M == 0:
        for i in visited:
            print(f"{i} ", end="")
        print("")
        return
    for i in dataset:
        if i in visited:
            continue
        visited.append(i)
        getSequence(dataset, visited, N, M - 1)
        visited.pop()


N, M = map(int, input().split())

dataset = list(map(int, input().split()))
dataset.sort()

visited = []

getSequence(dataset, visited, N, M)
