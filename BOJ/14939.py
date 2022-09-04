"""
14939번 불 끄기
"""

ALL_TURNED_ON = (1 << 100) - 1
bulbs = 0

for _ in range(10):
    line = input().replace("O", "0")
    line = line.replace("#", "1")

    bulbs = bulbs * 2**10 + int(line, 2)

dir = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]


def checkBorder(idx):
    if idx < 0 or idx >= 100:
        return False
    return True


def toggle(idx):
    global bulbs
    row, col = idx // 10, idx % 10

    for d in dir:
        nextRow = row + d[0]
        nextCol = col + d[1]
        if checkBorder(nextRow * 10 + nextCol):
            bulbs ^= 1 << (100 - nextRow * 10 + nextCol + 1)


minPress = float("inf")


def pressButton(idx, deep):
    if bulbs == ALL_TURNED_ON:
        if deep < minPress:
            minPress = deep
        return
    for next in range(idx + 1, 100):
        toggle(next)
        pressButton(next, deep + 1)
        toggle(next)


test = int("111111111", 2)

test ^= 1 << (9 - (2 * 3 + 3))

pressButton(-1, 0)

print()
