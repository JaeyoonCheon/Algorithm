"""
14939번 불 끄기

1.  처음 접근법은 100칸 모두를 껐다 켜보면서 모든 칸에 대해 경우의 수를 세 보려고 했으나
    이론상 완전탐색 시 2^100의 경우의 수가 나오므로, 완전탐색은 불가능하다고 생각이 된다.
    
2.  일단 전구의 1줄을 껐다 켜보면서 과정을 진행해 보면, 0번 전구부터 9번 전구까지 끄거나 켜는 작업을
    진행했을 때 그 아랫줄의 전구들은 윗줄의 전구가 켜져 있을 때 무조건 눌러 윗줄의 전구를
    꺼야만 한다.
    따라서 첫 줄의 전구 0~9번을 조작한 2^10가지의 완전탐색의 경우에 2~10번 줄의 전구들은 누르는 것이
    확정된 상태이므로, 1024번의 경우를 탐색하면 된다.
    
3.  2차원 배열로 전구를 구현하지 않고 1차원으로 구현했으며, 누르면 토글되는 5지점의
    전구들을 비트마스킹을 이용해 XOR연산으로 토글해 준다.
    이 때, 토글의 범위가 행을 넘어가는 경우(9번 열에서 오른쪽이나 0번 열에서 왼쪽)
    넘어가지 않도록 조정해 주어야 정확한 결과를 얻을 수 있다.
"""

import sys

ALL_TURNED_OFF = 0
bulbs = 0

for _ in range(10):
    line = input().replace("O", "1")
    line = line.replace("#", "0")

    bulbs = bulbs * 2**10 + int(line, 2)

dir = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]


def checkBorder(idx):
    if idx < 0 or idx >= 100:
        return False
    return True


def toggle(idx):
    global bulbs
    cand = [idx, idx + 1, idx - 1, idx - 10, idx + 10]
    if idx % 10 == 9:
        cand = [idx, idx - 1, idx - 10, idx + 10]
    if idx % 10 == 0:
        cand = [idx, idx + 1, idx - 10, idx + 10]

    for d in cand:
        if checkBorder(d):
            bulbs ^= 1 << (100 - d - 1)


def toggleBulbs(idx, bulbs):
    cand = [idx, idx + 1, idx - 1, idx - 10, idx + 10]
    if idx % 10 == 9:
        cand = [idx, idx - 1, idx - 10, idx + 10]
    if idx % 10 == 0:
        cand = [idx, idx + 1, idx - 10, idx + 10]

    for d in cand:
        if checkBorder(d):
            bulbs ^= 1 << (100 - d - 1)

    return bulbs


minPress = float("inf")


def operation(bulbs, count):
    global minPress

    for next in range(10, 100):
        if bulbs & 1 << (100 - (next - 10) - 1) != 0:
            bulbs = toggleBulbs(next, bulbs)
            count += 1

    if bulbs == ALL_TURNED_OFF:
        if count < minPress:
            minPress = count
        return


def pressButton(idx, deep, count):
    if deep == 10:
        operation(bulbs, count)
        return
    pressButton(idx + 1, deep + 1, count)
    toggle(idx + 1)
    pressButton(idx + 1, deep + 1, count + 1)
    toggle(idx + 1)


pressButton(-1, 0, 0)

if minPress != float("inf"):
    print(minPress)
else:
    print(-1)
