"""
    lv.2 삼각 달팽이
    
    1.  정삼각형에 반 시계 방향으로 외곽을 돌며 1~n까지의 수를 채워넣는 문제. 
        배열에 구현해 푸는 것이 빠르므로 왼쪽으로 정렬해 직각삼각형으로 만들어 풀이.
    2.  하, 우, 좌상의 3가지 방향을 지정한 뒤 삼각형 범위를 벗어나거나 진행 방향에 숫자가 없을 때 진행하도록 설정.
"""


def checkBorder(n, x, y):
    if x < 0 or x > n - 1 or y < 0 or y > x:
        return False
    return True


def solution(n):
    answer = []

    block = [[False] * n for _ in range(n)]

    dx = [1, 0, -1]
    dy = [0, 1, -1]

    num = 1
    dir = 0
    isEnd = False

    x, y = 0, 0

    while not isEnd:
        block[x][y] = num
        num = num + 1

        for i in range(3):
            nx, ny = x + dx[(dir + i) % 3], y + dy[(dir + i) % 3]

            if checkBorder(n, nx, ny) and not block[nx][ny]:
                x, y = nx, ny

                if i > 0:
                    dir = (dir + i) % 3
                break

            if i == 2:
                isEnd = True

    for i in range(n):
        for j in range(i + 1):
            answer.append(block[i][j])

    return answer


solution(4)
