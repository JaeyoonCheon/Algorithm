"""
3085 사탕 게임

1. '인접한' 두 칸 자리 교체
-> 우측 혹은 아래 2가지 경우만 고려하면 됨. 대각선은 고려 x

2. 마찬가지로 교체된 격자에서 가로/세로 방향으로만 연속된 사탕의 갯수 파악하면 됨

백준에서 python3로는 통과 x, pypy3로는 통과.

** 대각선은 고려하지 않으므로 작성한 코드는 주석 처리함
"""


def checkBorder(x, y, size):
    if x < 0 or y < 0:
        return False
    if x >= size or y >= size:
        return False
    return True


def checkSeq(candy, x, y, size):
    max = 1
    color = candy[x][y]

    cur = 1
    for i in range(x + 1, size):
        if checkBorder(i, y, size):
            if candy[i][y] == color:
                cur += 1
            else:
                break
        else:
            break
    for i in range(x - 1, -1, -1):
        if checkBorder(i, y, size):
            if candy[i][y] == color:
                cur += 1
            else:
                break
        else:
            break

    if max < cur:
        max = cur

    cur = 1
    for i in range(y + 1, size):
        if checkBorder(x, i, size):
            if candy[x][i] == color:
                cur += 1
            else:
                break
        else:
            break
    for i in range(y - 1, -1, -1):
        if checkBorder(x, i, size):
            if candy[x][i] == color:
                cur += 1
            else:
                break
        else:
            break

    if max < cur:
        max = cur

    # cur = 1
    # curX = x + 1
    # curY = y + 1
    # while checkBorder(curX, curY, size):
    #     if candy[curX][curY] == color:
    #         cur += 1
    #         curX += 1
    #         curY += 1
    #     else:
    #         break

    # curX = x - 1
    # curY = y - 1
    # while checkBorder(curX, curY, size):
    #     if candy[curX][curY] == color:
    #         cur += 1
    #         curX -= 1
    #         curY -= 1
    #     else:
    #         break

    # if max < cur:
    #     max = cur

    # cur = 1
    # curX = x + 1
    # curY = y - 1
    # while checkBorder(curX, curY, size):
    #     if candy[curX][curY] == color:
    #         cur += 1
    #         curX += 1
    #         curY -= 1
    #     else:
    #         break

    # curX = x - 1
    # curY = y + 1
    # while checkBorder(curX, curY, size):
    #     if candy[curX][curY] == color:
    #         cur += 1
    #         curX -= 1
    #         curY += 1
    #     else:
    #         break

    # if max < cur:
    #     max = cur

    return max


def swap(board, x1, y1, x2, y2):
    temp = board[x1][y1]
    board[x1][y1] = board[x2][y2]
    board[x2][y2] = temp


def findMaxCount(board, size):
    maxCount = 0
    for i in range(size):
        for j in range(size):
            # print(f"x: {i}, y: {j}")
            num = checkSeq(board, i, j, size)
            if maxCount < num:
                maxCount = num
    return maxCount


def swap2Block(candy, size):
    maxCount = 0
    temp = []
    for i in range(size):
        for j in range(size):
            temp = candy.copy()

            if checkBorder(i + 1, j, size):
                swap(temp, i, j, i + 1, j)
                result = findMaxCount(temp, size)
                if maxCount < result:
                    maxCount = result
                swap(temp, i, j, i + 1, j)

            # if checkBorder(i + 1, j + 1, size):
            #     swap(temp, i, j, i + 1, j + 1)
            #     result = findMaxCount(temp, size)
            #     if maxCount < result:
            #         maxCount = result
            #     swap(temp, i, j, i + 1, j + 1)

            if checkBorder(i, j + 1, size):
                swap(temp, i, j, i, j + 1)
                result = findMaxCount(temp, size)
                if maxCount < result:
                    maxCount = result
                swap(temp, i, j, i, j + 1)

            # if checkBorder(i - 1, j - 1, size):
            #     swap(temp, i, j, i - 1, j - 1)
            #     result = findMaxCount(temp, size)
            #     if maxCount < result:
            #         maxCount = result
            #     swap(temp, i, j, i - 1, j - 1)

    return maxCount


size = int(input())

candy = []

for _ in range(size):
    candy.append(list(input()))


print(swap2Block(candy, size))
