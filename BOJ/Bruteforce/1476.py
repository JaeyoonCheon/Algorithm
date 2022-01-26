"""
1476 날짜계산
"""


def check(E, S, M, cur):
    if E == cur[0] and S == cur[1] and M == cur[2]:
        return True
    else:
        return False


def goFirst(E, S, M):
    cur = [0, 0, 0]
    count = 0

    while True:
        for i in range(len(cur)):
            cur[i] += 1
        count += 1
        if check(E, S, M, cur):
            break
        if cur[0] >= 15:
            cur[0] = cur[0] % 15
        if cur[1] >= 28:
            cur[1] = cur[1] % 28
        if cur[2] >= 19:
            cur[2] = cur[2] % 19
    print(count)


E, S, M = map(int, input().split())
goFirst(E, S, M)
