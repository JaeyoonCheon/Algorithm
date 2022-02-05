"""
14500 테트로미노

나올 수 있는 모양
1. 1자 2개
2. 정사각형 1개
3. ㄹ자 4개(대칭 * 회전 2)
4. 요철 4개
5. ㄴ자 8개

총 19가지 경우의 수
"""


def checkBorder(width, height, x, y):
    if x < 0 or x >= height:
        return False
    if y < 0 or y >= width:
        return False
    return True


def pushBlock(puzzle, width, height, offsets):
    maxSum = 0

    for offset in offsets:
        for i in range(height):
            for j in range(width):
                partialSum = 0
                for disp in offset:
                    x = i + disp[0]
                    y = j + disp[1]
                    if not checkBorder(width, height, x, y):
                        break
                    partialSum += puzzle[x][y]
                if partialSum > maxSum:
                    maxSum = partialSum
                continue

    return maxSum


offsets = [
    # 1자
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    # 정사각형
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    # ㄹ자
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (-1, 0), (-1, 1), (-2, 1)],
    [(0, 0), (0, 1), (-1, 1), (-1, 2)],
    # ㄴ자
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (-1, 2)],
    [(0, 0), (-1, 0), (-2, 0), (-2, -1)],
    [(0, 0), (0, -1), (0, -2), (1, -2)],
    [(0, 0), (1, 0), (2, 0), (2, -1)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (-1, 0), (-2, 0), (-2, 1)],
    [(0, 0), (0, -1), (0, -2), (-1, -2)],
    # 요철
    [(0, 0), (0, 1), (0, 2), (-1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (-1, 0), (-2, 0), (-1, -1)],
]


height, width = map(int, input().split())
puzzle = [list(map(int, input().split())) for _ in range(height)]

print(pushBlock(puzzle, width, height, offsets))
