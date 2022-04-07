"""
7576번 토마토

1.  익지 않은 토마토가 익은 토마토와 인접해 있으면 1일 후 익는다.

2.  익은 토마토 여러 개로부터 동시에 인접한 익지 않은 토마토들이 익는다.

3.  풀이 전략
    1)  모든 칸에서 익은 토마토를 대상으로 BFS를 실행
        다만, 초기에 익은 토마토가 1개가 아닐 수 있으므로,
        초기 좌표를 설정하는 것이 아닌 BFS 실행 후 익은 토마토를 큐에 삽입
    2)  BFS에 의해 인접한 모든 토마토가 익었을 떄(큐가 비었을 경우)
        모든 칸에 익지 않은 토마토가 있는 지 판별
    3)  없으면 모두 익기까지의 날짜를 저장하여 출력
        있으면 -1 출력

4.  가로 - 세로 형식으로 입력이 들어옴. 순서 주의

5.  모든 토마토가 익어있거나 모두 비어있는 경우 등의 예외를 위해,
    BFS 검사 이전 익은 토마토가 존재하는지 검사 필요
    
6.  queue 라이브러리나 list를 이용한 큐는 시간제한에 걸림.
    collections의 deque를 사용해야 O(1), O(N) 시간복잡도로 통과 가능
"""

from collections import deque
import sys

M, N = map(int, sys.stdin.readline().split())

box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False] * M for _ in range(N)]

q = deque()


def check():
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0 and visited[i][j] == False:
                return False
    return True


def BFS():
    count = 1

    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                q.append((i, j, 1))
                visited[i][j] = True

    while q:
        curr = q.popleft()

        for i in range(4):
            x = curr[0] + dx[i]
            y = curr[1] + dy[i]

            if x < 0 or x >= N or y < 0 or y >= M:
                continue
            if box[x][y] == -1 or box[x][y] == 1:
                continue
            if visited[x][y] == True:
                continue
            if count < curr[2]:
                count = curr[2]

            visited[x][y] = True
            box[x][y] = 1
            q.append((x, y, curr[2] + 1))

    if check() == False:
        print("-1")
    else:
        print(count)


if check() == False:
    BFS()
else:
    print("0")
