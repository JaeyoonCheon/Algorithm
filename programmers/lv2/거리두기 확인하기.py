"""
    lv.2 거리두기 확인하기
    
    1.  격자의 P에서 맨하튼 거리 2 이내에서 갈 수 있는 P가 존재하는 지 확인하는 문제.
    2.  DFS/BFS로 풀이해도 되겠으나, 캐시 등의 번거로운 코드가 생기고, 맨하튼 거리 2의 간단한 경우의 수 밖에 없기 때문에
        모든 경우의 수를 체크해 풀이.
    3.  현재 풀이에서는 거리 1, 2의 4방향, 대각선 4방향 모두 확인하였으나 (0, 0)부터 (5, 5)까지 순서대로 확인하는 로직이기 때문에
        오른쪽/아래쪽 방향만 확인하면 풀이 가능할 것으로 생각됨.
"""


def checkBorder(x, y):
    if x < 0 or x >= 5 or y < 0 or y >= 5:
        return False
    return True


def check(place, players):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cx = [1, 1, -1, -1]
    cy = [1, -1, 1, -1]

    for player in players:
        x, y = player

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            nnx, nny = x + 2 * dx[i], y + 2 * dy[i]

            if not checkBorder(nx, ny):
                continue

            if place[nx][ny] == "P":
                return False

            if place[nx][ny] == "O":
                if not checkBorder(nnx, nny):
                    continue

                if place[nnx][nny] == "P":
                    return False

        for i in range(4):
            nx, ny = x + cx[i], y + cy[i]

            if not checkBorder(nx, ny):
                continue

            if place[nx][ny] == "P":
                if place[x][ny] != "X" or place[nx][y] != "X":
                    return False

    return True


def solution(places):
    answer = []

    for place in places:
        players = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    players.append((i, j))

        if not players:
            answer.append(1)
            continue

        if check(place, players):
            answer.append(1)
        else:
            answer.append(0)

    return answer


result = solution(
    [
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
    ]
)

print(result)
