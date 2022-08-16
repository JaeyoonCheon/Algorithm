"""
12852번 1로 만들기 2

1.  X에서 1로 3가지 연산을 통해 전파될 수 있는 최단 경로를 찾는 문제로,
    3가지 경로를 가지는 1차원 BFS문제로 해석하는 것이 가장 효율적이라고 생각된다.
    
2.  다만, 1차원 BFS로 최단 경로의 길이를 찾았을 때, X에서 1로 최단거리에 도달할 수 있는 경로 중
    아무 것이나 역추적해 출력해야 하므로 어떤 지점을 지날 때 최소의 step인 방법을 큐에서 뽑았을 경우
    해당 지점에 이전 지점/step을 기록해 놓고 1부터 역추적한다.
    
3.  역추적 시, 이전 지점에 기록된 정보들 중, 현재 step보다 1적은 정보들에서 아무 것이나 골라도
    무방하다. 결과적으로 X~1의 최단 경로인 조건만 충족하면 되므로 이 코드에서는 step-1인 가장 처음 만나는
    이전 지점으로 역추적해 X로 회귀하며 지나온 경로를 반전시켜 출력했다.    
"""

import collections

X = int(input())

pos = [[] for _ in range(X + 1)]

q = collections.deque()

q.append((X, 0))

while q:
    curr = q.popleft()

    if curr[0] == 1:
        break

    if curr[0] % 3 == 0:
        q.append((curr[0] // 3, curr[1] + 1))
        if pos[curr[0] // 3]:
            if curr not in pos[curr[0] // 3] and pos[curr[0] // 3][0][1] >= curr[1]:
                pos[curr[0] // 3].append(curr)
        else:
            pos[curr[0] // 3].append(curr)

    if curr[0] % 2 == 0:
        q.append((curr[0] // 2, curr[1] + 1))
        if pos[curr[0] // 2]:
            if curr not in pos[curr[0] // 2] and pos[curr[0] // 2][0][1] >= curr[1]:
                pos[curr[0] // 2].append(curr)
        else:
            pos[curr[0] // 2].append(curr)

    if curr[0] - 1 > 0:
        q.append((curr[0] - 1, curr[1] + 1))
        if pos[curr[0] - 1]:
            if curr not in pos[curr[0] - 1] and pos[curr[0] - 1][0][1] >= curr[1]:
                pos[curr[0] - 1].append(curr)
        else:
            pos[curr[0] - 1].append(curr)

result = []

while True:
    result.append(curr[0])
    if curr[0] == X:
        break

    for i in pos[curr[0]]:
        if i[1] == curr[1] - 1:
            curr = i
            break

result.reverse()

print(len(result) - 1)
for i in result:
    print(i, end=" ")
