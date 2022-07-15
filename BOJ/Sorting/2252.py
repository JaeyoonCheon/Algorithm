"""
2252번 줄 세우기

1.  주어진 N개의 노드들을 주어진 M개의 순서에 맞게 배열하는 문제.

2.  처음 생각한 방법은 1~N까지의 오름차순은 수열을 나열해놓고
    주어진 순서에 맞게 swap하는 과정을 반복해보는 것이었다.
    하지만 이 방법은 대강 잡아도 O(N^2) 시간 복잡도로 보이는데
    시간 효율적인 측면에서 좋지 않은 방법으로 생각되었다.

3.  다음 방법은 주어진 노드-순서를 방향 그래프로 생각하고
    초기 노드에서 시작해 끝 노드까지 지나가는 경로를 구하는 방법으로
    들어오는(income) 간선의 노드를 방문하지 않았다면 지나가지 못한다는 제약을 두면
    모든 순서를 지키면서 모든 노드를 지나가는 경로를 구할 수 있을 것으로 생각했다.
    이것이 곧 '위상정렬' 방법이다.

4.  세부적으로는 그래프를 만들어 각 노드마다의 income을 구하고
    항상 그 단계에서의 시작점은 income이 0인 노드부터 시작한다.
    경로에 해당 노드들을 넣고 그 노드에서 뻗어나갈 수 있는 노드들의 income을 하나 씩
    지워나가며 위 과정을 반복한다.
"""

import sys, collections

N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]
invertedG = [[] for _ in range(N + 1)]

for _ in range(M):
    _from, _to = map(int, sys.stdin.readline().split())

    G[_from].append(_to)
    invertedG[_to].append(_from)


income = [()]

for i in range(1, N + 1):
    income.append(len(invertedG[i]))

path = []

q = collections.deque()

step = 0

for i in range(1, N + 1):
    if income[i] == 0:
        q.append(i)
        path.append(i)

while q:
    curr = q.popleft()

    for nextNode in G[curr]:
        income[nextNode] -= 1
        if income[nextNode] == 0 and nextNode not in path and nextNode not in q:
            q.append(nextNode)
            path.append(nextNode)

for i in path:
    print(i, end=" ")
