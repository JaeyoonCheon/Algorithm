"""
15662번 톱니바퀴 2

1.  톱니바퀴는 1회 회전에 1:시계방향/-1:반시계방향으로 회전하게 되는데, 각 톱니에는 8개의 N극과 S극이 있다.
    3시/9시에 다른 톱니와 서로 맞닿은 부분에서 다른 톱니가 회전할 지 안할 지를 결정하게 되며
    맞닿은 부분의 극이 같으면 회전하지 않고 다르면 돌린 톱니바퀴와 다른 방향으로 회전하게 된다.
    
2.  구현할 때 톱니 자체는 가만히 놓고 12시 방향이 위치하는 인덱스를 top 리스트에 따로 저장하여
    처음 돌리는 톱니바퀴의 왼쪽/오른쪽을 1칸 씩 전진하면서 다음 12시 인덱스를 계산하여 rotate 리스트에
    저장하였다.
    
3.  rotate 배열에 원래 위치 + 움직이는 방향(부호 반대로하여 적용)을 계산하여 저장할 때,
    톱니바퀴의 톱니는 8개로 고정되어 있기 떄문에 8로 MOD 연산을 적용해 주어야 정상적으로 적용되며
    맞닿은 톱니끼리 비교할 때 맞닿은 위치를 계산하기 위해 top 값을 가져다 쓸 때에도
    8 MOD 연산을 적용해 주어야 한다.
    
4.  반드시 고려하여야 할 점은 톱니바퀴는 현실에서도 회전시키면 맞물린 톱니바퀴들은 동시에! 돌아간다.
    따라서 rotate 배열에 따로 변동된 값을 저장했으며, 처음 회전시킨 톱니는 제일 마지막에 회전시켜야 한다.
"""

T = int(input())

gear = [list(map(int, list(input()))) for _ in range(T)]

top = [0] * T

K = int(input())

operation = [list(map(int, input().split())) for _ in range(K)]

for iter in range(K):
    start = operation[iter][0] - 1
    direction = operation[iter][1]
    rotate = top.copy()

    tempDir = direction
    for i in range(start - 1, -1, -1):
        if gear[i + 1][(top[i + 1] - 2) % 8] != gear[i][(top[i] + 2) % 8]:
            rotate[i] = (top[i] + tempDir) % 8
        else:
            break
        tempDir *= -1

    tempDir = direction
    for i in range(start + 1, T):
        if gear[i - 1][(top[i - 1] + 2) % 8] != gear[i][(top[i] - 2) % 8]:
            rotate[i] = (top[i] + tempDir) % 8
        else:
            break
        tempDir *= -1

    rotate[start] = (top[start] + -1 * direction) % 8

    for i in range(T):
        top[i] = rotate[i]

    print("", end="")

count = 0

for i in range(T):
    if gear[i][top[i]] == 1:
        count += 1

print(count)
