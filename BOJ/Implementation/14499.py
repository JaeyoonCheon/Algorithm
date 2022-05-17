"""
14499번 주사위 굴리기

1.  문제 조건을 잘 읽자!!!!
    1)  주어진 좌표계를 뒤집어 생각해야 함.
        x, y가 데카르트 좌표계로 변환되므로 x가 가로 축, y가 세로 축이 되도록 조정
    2)  주어진 전개도를 바닥에 놓인 주사위라고 간주
        즉, 123456은 위치가 그대로 놓여 있는데 동서남북으로 주사위가 움직이면
        123456에 적힌 숫자가 달라진다고 생각해 보자.
    3)  지도에 0이 적혀있으면 주사위의 바닥면 수를 복사하고,
        지도에 0이 아닌 수가 적혀 있으면 그 수를 주사위의 바닥면에 복사한 후
        지도의 수를 0으로 만든다! <- 이 과정을 해주지 않아 고생
"""

N, M, y, x, K = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

operation = list(map(int, input().split()))

# 현재 수, 동, 서, 북, 남
dice = [0] * 7


def checkBorder(x, y, N, M):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    return True


def changeNumber():
    # 현재 주사위가 놓여 있는 지도 상의 위치의 수
    pos = maps[y][x]

    if pos != 0:
        dice[1] = pos
        maps[y][x] = 0
    else:
        maps[y][x] = dice[1]


changeNumber()

for move in range(K):
    # 동
    if operation[move] == 1:
        x += 1
        if checkBorder(x, y, N, M) == False:
            x -= 1
            continue
        tempDice = dice.copy()

        dice[1] = tempDice[3]
        dice[2] = tempDice[2]
        dice[3] = tempDice[6]
        dice[4] = tempDice[1]
        dice[5] = tempDice[5]
        dice[6] = tempDice[4]
        changeNumber()
    # 서
    elif operation[move] == 2:
        x -= 1
        if checkBorder(x, y, N, M) == False:
            x += 1
            continue
        tempDice = dice.copy()

        dice[1] = tempDice[4]
        dice[2] = tempDice[2]
        dice[3] = tempDice[1]
        dice[4] = tempDice[6]
        dice[5] = tempDice[5]
        dice[6] = tempDice[3]
        changeNumber()
    # 북
    elif operation[move] == 3:
        y -= 1
        if checkBorder(x, y, N, M) == False:
            y += 1
            continue
        tempDice = dice.copy()

        dice[1] = tempDice[2]
        dice[2] = tempDice[6]
        dice[3] = tempDice[3]
        dice[4] = tempDice[4]
        dice[5] = tempDice[1]
        dice[6] = tempDice[5]
        changeNumber()
    # 남
    else:
        y += 1
        if checkBorder(x, y, N, M) == False:
            y -= 1
            continue
        tempDice = dice.copy()

        dice[1] = tempDice[5]
        dice[2] = tempDice[1]
        dice[3] = tempDice[3]
        dice[4] = tempDice[4]
        dice[5] = tempDice[6]
        dice[6] = tempDice[2]
        changeNumber()

    print(dice[6])
