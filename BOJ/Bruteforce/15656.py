"""
15656번 N과 M (7)

1. 입력된 자연수 set을 정렬 저장
2. 오름차순이 아닐 경우 가지치기하는 조건 제거
3. 중복조건 제거
"""


def getSequence(dataset, visited, N, M):
    if M == 0:
        for i in visited:
            print(f"{i} ", end="")
        print("")
        return
    for i in dataset:
        visited.append(i)
        getSequence(dataset, visited, N, M - 1)
        visited.pop()


N, M = map(int, input().split())

dataset = list(map(int, input().split()))
dataset.sort()

visited = []

getSequence(dataset, visited, N, M)
