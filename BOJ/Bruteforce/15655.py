"""
15655번 N과 M (6)

1. 입력된 자연수 set을 정렬 저장
2. 오름차순이 아닐 경우 가지치기하는 조건 추가
"""


def getSequence(dataset, visited, N, M):
    if M == 0:
        for i in visited:
            print(f"{i} ", end="")
        print("")
        return
    for i in dataset:
        flag = False
        if i in visited:
            continue
        for j in visited:
            if i < j:
                flag = True
        if flag == True:
            continue
        visited.append(i)
        getSequence(dataset, visited, N, M - 1)
        visited.pop()


N, M = map(int, input().split())

dataset = list(map(int, input().split()))
dataset.sort()

visited = []

getSequence(dataset, visited, N, M)
