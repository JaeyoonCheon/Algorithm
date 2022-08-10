"""
9466번 텀 프로젝트

1.  주어진 학생(노드) 간 사이클을 이루면 사이클에 포함된 노드들은 한 팀이 되는 조건.

2.  학생들을 dfs로 순회하면서 사이클(순회 중 방문했던 지점 방문)을 발견하면
    사이클에 포함된 수 만큼 팀에 포함되지 못한 사람의 수를 차감한다.

3.  초기에는 dfs로 구현하였으나, 그래프 순회 중 사이클 조건에서
    초기 시작지점-끝 지점이 아닌 중간 순회지점-끝 지점이 이루는 사이클을 방문처리하기 위해
    더 용이한 bfs로 구현
"""

import sys, collections

T = int(input())

for _ in range(T):
    N = int(input())

    student = list(map(int, sys.stdin.readline().split()))
    student.insert(0, 0)

    visited = [False] * (N + 1)
    nonTeam = N

    def checkCycle(point):
        global nonTeam
        q = collections.deque()
        pathQ = collections.deque()

        visited[point] = True
        q.append(point)
        curr = point

        while q:
            next = student[curr]

            if not visited[next]:
                visited[next] = True
                q.append(next)
                curr = next
            else:
                setQ = set(q)
                if next in setQ:
                    while True:
                        top = q.pop()
                        nonTeam -= 1
                        if top == next:
                            break
                    if q:
                        while q:
                            top = q.pop()
                            visited[top] = False
                else:
                    break

    for point in range(1, N + 1):
        if not visited[point]:
            checkCycle(point)

    print(nonTeam)
