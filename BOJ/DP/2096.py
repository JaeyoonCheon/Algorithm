"""
2096번 내려가기

1.  어떤 줄 i에서 1번, 2번, 3번 칸 중 하나를 선택했다면,
    다음 줄 i+1로 바로 밑 칸이나 바로 밑칸의 양 옆칸만 내려갈 수 있다.
    
2.  DP로 접근하기 위해, 반대로 생각할 필요가 있다.
    윗칸에서 내려갈 때의 아래칸의 가능한 경우가 아닌, 아래칸을 결정할 때
    가능한 윗칸의 경우를 생각해 보면 쉽게 생각할 수 있다.
    
3.  1보다 큰 층의 각 칸의 바로 윗 칸이나 바로 윗 칸의 양 옆 중 조건에 맞는 수를 현재 위치의 수와
    더해 만들어 지므로 점화식을 구성할 수 있다.
    
4.  메모리 관리를 위해, 최소/최대 칸을 구성한 DP 리스트는 단 두 줄만 있어도 과거/현재 정보를 저장할
    수 있으므로 줄여서 만들어야 한다.
"""

import sys

N = int(input())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

minDP = [[0, 0, 0], [0, 0, 0]]
minDP[0] = board[0].copy()

maxDP = [[0, 0, 0], [0, 0, 0]]
maxDP[0] = board[0].copy()

for i in range(1, N):
    level = i % 2
    minDP[level][0] = (
        min(minDP[(level - 1) % 2][0], minDP[(level - 1) % 2][1]) + board[i][0]
    )
    maxDP[level][0] = (
        max(maxDP[(level - 1) % 2][0], maxDP[(level - 1) % 2][1]) + board[i][0]
    )

    minDP[level][1] = (
        min(
            minDP[(level - 1) % 2][0],
            minDP[(level - 1) % 2][1],
            minDP[(level - 1) % 2][2],
        )
        + board[i][1]
    )
    maxDP[level][1] = (
        max(
            maxDP[(level - 1) % 2][0],
            maxDP[(level - 1) % 2][1],
            maxDP[(level - 1) % 2][2],
        )
        + board[i][1]
    )

    minDP[level][2] = (
        min(minDP[(level - 1) % 2][1], minDP[(level - 1) % 2][2]) + board[i][2]
    )
    maxDP[level][2] = (
        max(maxDP[(level - 1) % 2][1], maxDP[(level - 1) % 2][2]) + board[i][2]
    )

print(f"{max(maxDP[(N-1)%2])} {min(minDP[(N-1)%2])}")
