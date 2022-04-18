"""
14503번 로봇 청소기
"""

N, M = map(int, input().split())

r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]

cleaned = [[False] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 현재 위치를 청소
cleaned[r][c] = True
count = 1

while True:
    turn = False
    # 왼쪽으로 4번 회전
    for move in range(4):
        # 왼쪽이 빈 공간인가?
        rx = r + dx[(d + 3) % 4]
        cy = c + dy[(d + 3) % 4]
        d = (d + 3) % 4

        if rx >= 0 and rx < N and cy >= 0 and cy < M:
            if room[rx][cy] != 1:
                # 왼쪽이 이미 청소된 공간인가?
                if cleaned[rx][cy] == False:
                    r = rx
                    c = cy
                    # 현재 위치를 청소
                    cleaned[r][c] = True
                    count += 1
                    turn = True
                    break

    # 왼쪽으로 4번 돌았을 경우
    if turn == False:
        # 바로 뒤쪽이 벽일 경우
        if room[r - dx[d]][c - dy[d]] == 1:
            break
        # 아닐 경우
        else:
            r = r - dx[d]
            c = c - dy[d]


print(count)
