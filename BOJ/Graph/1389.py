"""
1389번 케빈 베이컨의 6단계 법칙

1.  bfs를 활용한 그래프 최단거리 응용 문제.

2.  풀이하는데 시간이 오래 걸렸는데, collections의 deque를 사용하여 구현한 코드가
    큐가 아닌 스택의 동작과정을 수행하고 있어 결과값이 다르게 발생했다.
    인지하는 데 오래 걸린 이유는 스택 또한 중간 결과가 유사하게 나와 동작 반례를
    늦게 알았기 때문
"""

import collections

N, M = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    one, another = map(int, input().split())

    graph[one][another] = 1
    graph[another][one] = 1


def bfs(number):
    q = collections.deque()
    check = [0] * (N + 1)

    q.append((number, 0))
    check[number] = 0

    while q:
        curr = q.popleft()

        for i in range(1, N + 1):
            if i == curr[0]:
                continue
            if check[i] != 0:
                continue
            if graph[curr[0]][i] == 1:
                q.append((i, curr[1] + 1))
                if check[i] == 0:
                    check[i] = curr[1] + 1

    return sum(check)


kbn = []

for i in range(1, N + 1):
    kbn.append(bfs(i))

minimum = min(kbn)

for i, v in enumerate(kbn):
    if v == minimum:
        print(i + 1)
        break
