"""
20055번 컨베이어 벨트 위의 로봇

1.  주어지는 컨베이어 벨트는 1~N까지 위쪽이고 N+1~2N부터는 밑으로 들어가는
    옆에서 본 컨베이어 벨트를 1차원으로 나타낸 것이다.
    
2.  주어지는 조건을 정확히 수행하면 통과 가능하다.
    1)  컨베이어 벨트가 회전할 때 그 위의 로봇 또한 같이 움직인다.
    2)  로봇은 N위치에 도달하는 순간 내린다
    3)  로봇이 전진하는 순서는 가장 먼저 탄 순서(FIFO)이며,
        한번에 1칸씩만 전진한다.
"""

N, K = map(int, input().split())

A = list(map(int, input().split()))
robots = [False] * 2 * N


def check():
    count = 0
    for i in A:
        if i == 0:
            count += 1
        if count >= K:
            return False
    return True


def rotate():
    first = A[2 * N - 1]

    for i in range(2 * N - 1, 0, -1):
        A[i] = A[i - 1]
        robots[i] = robots[i - 1]

    A[0] = first
    robots[0] = False


step = 0

while check():
    step += 1
    rotate()
    if robots[N - 1] == True:
        robots[N - 1] = False

    for i in range(2 * N - 1, 0, -1):
        if A[i] > 0 and robots[i] == False:
            if robots[i - 1] == True:
                robots[i - 1] = False
                robots[i] = True
                A[i] -= 1

        if robots[N - 1] == True:
            robots[N - 1] = False

    if A[0] > 0:
        robots[0] = True
        A[0] -= 1

print(step)
