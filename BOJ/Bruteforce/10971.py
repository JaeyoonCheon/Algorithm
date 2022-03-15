"""
10971번 외판원 순회 2

1. TSP 문제 + 모든 순열에 대한 검사
python 내장 모듈 itertools를 불러와 사용했으며,
python3로는 일반적인 완전탐색에 대한 경과시간이 2초를 초과함.
따라서 조금 더 효율적인 pypy3을 사용하면 통과
"""

import itertools


def TSP(N, node):
    minCost = 11000001
    flag = False
    for i in itertools.permutations(range(N), N):
        cost = 0
        for j in range(N - 1):
            if node[i[j]][i[j + 1]] == 0:
                flag = True
                break
            cost += node[i[j]][i[j + 1]]
        if node[i[j + 1]][i[0]] == 0:
            flag = True
        cost += node[i[j + 1]][i[0]]

        if flag == True:
            flag = False
            continue

        if cost < minCost:
            minCost = cost

    return minCost


N = int(input())
node = []

for _ in range(N):
    node.append(list(map(int, input().split())))

print(TSP(N, node))
