"""
2623번 음악 프로그램

1.  PD마다 각자 생각하는 가수들의 순서가 주어지는데,
    이것을 취합하여 가능한 경우의 모든 가수에 대한 순서를 만들어내는 문제.

2.  각각의 순서는 앞의 번호의 가수에서 뒤의 번호의 가수로 전파되는 방향 그래프로
    생각할 수 있을 것이다.
    따라서, 모든 주어지는 순서들을 하나의 방향 그래프로 만들어내고
    그 그래프의 시작점으로부터 끝 점까지의 순서를 정렬하기에 효율적인
    위상 정렬 알고리즘을 적용해보기로 했다.

3.  앞서 모든 순서를 주어진대로 방향 그래프로 만들면서, 각각의 가수에 대해
    자신으로 전파되는 가수 번호가 있다면 incomes[가수]를 하나 늘려
    income 가지를 하나 늘려준다.

4.  위상정렬을 위해 큐를 만들고, incomes가 0인 가수를 모두 큐에 넣는다.
    이후 하나씩 큐에서 뽑아 그 가수에서 전파되는 다른 방문하지않은 가수가 있다면
    그 가수의 incomes를 하나 줄인다.
    만약, incomes가 0이 될 경우 큐에 넣고 위의 과정을 반복하면 위상정렬을 할 수 있다.

5.  순서가 잘못되어 정렬을 할 수 없는 경우는 일방향이 아닌 사이클이 만들어져
    계속 순환하는 경우로, 이 때 사이클에 걸리면 incomes가 계속 줄어들어
    모든 가수 N을 한번 씩 둘러보기 전에 큐에 남은 가수가 없게 되므로 이 때 0을 출력한다.
"""

import sys, collections

N, M = map(int, input().split())

incomes = [0] * (N + 1)
G = [[] for _ in range(N + 1)]

for i in range(M):
    inputs = list(map(int, sys.stdin.readline().split()))

    for j in range(1, len(inputs) - 1):
        G[inputs[j]].append(inputs[j + 1])
        incomes[inputs[j + 1]] += 1

q = collections.deque()

for i in range(1, N + 1):
    if incomes[i] == 0:
        q.append(i)

order = []

for person in range(1, N + 1):
    if not q:
        print(0)
        break

    curr = q.popleft()
    order.append(curr)

    for i in G[curr]:
        if i not in order:
            incomes[i] -= 1
            if incomes[i] == 0:
                q.append(i)

if len(order) == N:
    for person in order:
        print(person)
