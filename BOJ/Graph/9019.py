"""
9019번 DSLR

1.  가장 처음 문제를 봤을 때는 4자리 레지스터에 해당하는 변수 4개를 가지고
    직접 조작하면서 모든 경우의 수를 탐색해야 하나 라고 생각했다.
    하지만 시간 제한이 6초라고는 하지만 제한 없는 모든 경우의 수를 탐색하는 것은
    2^n 시간복잡도이므로 제외하도록 했다.
    
2.  문제의 힌트는 
    "주어진 서로 다른 두 정수 A와 B(A ≠ B)에 대하여 A를 B로 바꾸는 최소한의 명령어를 생성하는 프로그램"
    에서 최소한 이라는 단어이다. 어떤 지점(A)에서 목표 지점(B)까지 최소한의 움직임을 찾는 것이므로
    BFS 최단 거리 문제라고 생각할 수 있다.
    
3.  따라서, 0~9999 사이의 수를 방문했는지 체크하고 시작 수 A로부터 4가지 명령을 통해 만들어진
    4개 수를 큐에 넣고 반복적으로 BFS를 수행하다가 목표 수에 도달하면 출력
    
4.  처음 시도에는 지나 온 경로를 큐에 문자열로 저장하였는데, 문자열 핸들링의 속도가 많이 느려
    방문한 지점을 기록하는 visited 배열에 이전 위치를 저장하여 경로를 역추적하는 방식으로
    시간을 줄였다.
"""

import collections

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    q = collections.deque()
    visited = [0] * 10000

    q.append((A, ""))
    visited[A] = (-1, "")

    while q:
        curr = q.popleft()

        if curr[0] != B:
            num = (curr[0] * 2) % 10000
            if not visited[num]:
                q.append((num, "D"))
                visited[num] = (curr[0], "D")

            num = (curr[0] - 1) % 10000
            if not visited[num]:
                q.append((num, "S"))
                visited[num] = (curr[0], "S")

            num = (curr[0] % 1000) * 10 + curr[0] // 1000
            if not visited[num]:
                q.append((num, "L"))
                visited[num] = (curr[0], "L")

            num = curr[0] // 10 + curr[0] % 10 * 1000
            if not visited[num]:
                q.append((num, "R"))
                visited[num] = (curr[0], "R")
        else:
            path = ""
            i = curr[0]
            while visited[i][0] != -1:
                path = path + visited[i][1]
                i = visited[i][0]

            print(path[::-1])
