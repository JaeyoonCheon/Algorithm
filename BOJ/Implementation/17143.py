"""
17143번 낚시왕

1.  구현 문제에 속하는 문제로, 문제에서 제시하는 과정을 잘 구현하면 웬만한 테스트케이스는
    통과 가능.

2.  중간 시도에서 계속 막혔던 부분은 낚시왕이 낚시를 할 때 가장 위의 물고기를 고르는 과정에서
    초기값 top이 행의 길이보다 더 작은 (2*열의 길이)인 경우로 세팅해 놓아 예외인 경우가 발생했기 때문이었다.
"""

import sys

R, C, M = map(int, input().split())

sharks = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

fisher = -1
fished = 0


def fishing(pos):
    global fished, sharks
    top = R * 2
    idx = -1

    for i, shark in enumerate(sharks):
        x, y = shark[0], shark[1]

        if pos == y:
            if x < top:
                top = x
                idx = i

    if idx != -1:
        fished += sharks[idx][4]
        sharks.pop(idx)
        return
    else:
        return


def checkBorder(x, y):
    if x < 1 or x > R or y < 1 or y > C:
        return True
    return False


def reverseDir(dir):
    if dir == 1:
        return 2
    elif dir == 2:
        return 1
    elif dir == 3:
        return 4
    elif dir == 4:
        return 3


def moving():
    global sharks

    for shark in sharks:
        r, c, s, d, z = shark[0], shark[1], shark[2], shark[3], shark[4]

        for move in range(s):
            tempR, tempC = r + dx[d], c + dy[d]
            if checkBorder(tempR, tempC):
                d = reverseDir(d)

            r, c = r + dx[d], c + dy[d]

        shark[0], shark[1], shark[3] = r, c, d

    sharks = sorted(sharks, key=lambda x: (x[0], x[1], -x[4]))

    idx = 0

    while idx != len(sharks) - 1 and len(sharks) > 0:
        next = idx + 1
        if next >= len(sharks):
            break

        if sharks[idx][0] == sharks[next][0] and sharks[idx][1] == sharks[next][1]:
            sharks.pop(next)
        else:
            idx += 1


def sequence():
    for i in range(1, C + 1):
        fishing(i)
        moving()

    print(fished)


sequence()
