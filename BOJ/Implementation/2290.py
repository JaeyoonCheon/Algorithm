"""
2290번 LCD Test

1.  노가다 문제.
    좌표, 각 숫자의 시작 위치, 가로/세로가 나타나는 위치 등의 좌표를 신경써서 풀어야 함
"""

s, n = map(int, input().split())

digit = list(map(int, list(str(n))))

lcd = [[" "] * ((s + 3) * len(digit)) for _ in range(2 * s + 3)]


def showDigit(type, s, pivot):
    if type == "0":
        for i in range(1, s + 1):
            lcd[0][pivot + i] = "-"
            lcd[2 * s + 2][pivot + i] = "-"
        for i in range(2 * s + 3):
            if i == 0 or i == s + 1 or i == 2 * s + 2:
                continue
            lcd[i][pivot] = "|"
            lcd[i][s + pivot + 1] = "|"
    elif type == "1":
        for i in range(2 * s + 3):
            if i == 0 or i == s + 1 or i == 2 * s + 2:
                continue
            lcd[i][s + pivot + 1] = "|"
    elif type == "2":
        for i in range(1, s + 1):
            lcd[0][pivot + i] = "-"
            lcd[s + 1][pivot + i] = "-"
            lcd[2 * s + 2][pivot + i] = "-"
        for i in range(s + 1):
            if i == 0 or i == s + 1 or i == 2 * s + 2:
                continue
            lcd[i][s + pivot + 1] = "|"
        for i in range(s + 1, 2 * s + 3):
            if i == 0 or i == s + 1 or i == 2 * s + 2:
                continue
            lcd[i][pivot] = "|"
    elif type == "3":
        for i in range(1, s + 1):
            lcd[0][pivot + i] = "-"
            lcd[s + 1][pivot + i] = "-"
            lcd[2 * s + 2][pivot + i] = "-"
        for i in range(2 * s + 3):
            if i == 0 or i == s + 1 or i == 2 * s + 2:
                continue
            lcd[i][s + pivot + 1] = "|"
    elif type == "4":
        for i in range(1, s + 1):
            lcd[s + 1][pivot + i] = "-"
        for i in range(s + 1):
            if i == 0 or i == s + 1 or i == 2 * s + 2:
                continue
            lcd[i][pivot] = "|"
            lcd[i][s + pivot + 1] = "|"
        for i in range(s + 1, 2 * s + 3):
            if i == 0 or i == s + 1 or i == 2 * s + 2:
                continue
            lcd[i][s + pivot + 1] = "|"
    elif type == "5":
        for i in range(1, s + 1):
            lcd[0][pivot + i] = "-"
            lcd[s + 1][pivot + i] = "-"
            lcd[2 * s + 2][pivot + i] = "-"
        for i in range(s + 1):
            if i == 0 or i == s + 1 or i == 2 * s + 2:
                continue
            lcd[i][pivot] = "|"
        for i in range(s + 1, 2 * s + 3):
            if i == 0 or i == s + 1 or i == 2 * s + 2:
                continue
            lcd[i][s + pivot + 1] = "|"
    elif type == "6":
        for i in range(1, s + 1):
            lcd[0][pivot + i] = "-"
            lcd[s + 1][pivot + i] = "-"
            lcd[2 * s + 2][pivot + i] = "-"
        for i in range(s + 1):
            if i == 0 or i == s + 1 or i == 2 * s + 2:
                continue
            lcd[i][pivot] = "|"
        for i in range(s + 1, 2 * s + 3):
            if i == 0 or i == s + 1 or i == 2 * s + 2:
                continue
            lcd[i][pivot] = "|"
            lcd[i][s + pivot + 1] = "|"
    elif type == "7":
        for i in range(1, s + 1):
            lcd[0][pivot + i] = "-"
        for i in range(2 * s + 3):
            if i == 0 or i == s + 1 or i == 2 * s + 2:
                continue
            lcd[i][s + pivot + 1] = "|"
    elif type == "8":
        for i in range(1, s + 1):
            lcd[0][pivot + i] = "-"
            lcd[s + 1][pivot + i] = "-"
            lcd[2 * s + 2][pivot + i] = "-"
        for i in range(2 * s + 3):
            if i == 0 or i == s + 1 or i == 2 * s + 2:
                continue
            lcd[i][pivot] = "|"
            lcd[i][s + pivot + 1] = "|"
    elif type == "9":
        for i in range(1, s + 1):
            lcd[0][pivot + i] = "-"
            lcd[s + 1][pivot + i] = "-"
            lcd[2 * s + 2][pivot + i] = "-"
        for i in range(s + 1):
            if i == 0 or i == s + 1 or i == 2 * s + 2:
                continue
            lcd[i][pivot] = "|"
            lcd[i][s + pivot + 1] = "|"
        for i in range(s + 1, 2 * s + 3):
            if i == 0 or i == s + 1 or i == 2 * s + 2:
                continue
            lcd[i][s + pivot + 1] = "|"


pos = 0

for i in range(len(digit)):
    showDigit(str(digit[i]), s, pos)
    pos += s + 3

for i in range(2 * s + 3):
    for j in range(((s + 3) * len(digit))):
        print(lcd[i][j], end="")
    print()
