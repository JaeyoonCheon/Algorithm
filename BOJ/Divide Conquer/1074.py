"""
1074번 Z

1.  문제에서 제시하는 Z모양은 최소 단위가 2x2 정사각형에서 발생하고,
    2^N 길이의 정사각형을 4분할한 것에 대해 반복적으로 수행되고 있는 것을 알 수 있다.
    따라서, 가장 큰 곳부터 시작하여 4-1-2-3 사분면 순서대로 좌표를 넘기고
    수행하는 길이를 절반으로 줄여 길이가 2가 되면 숫자를 기록하는 방식으로 풀이하였다.
    하지만 배열로 해당 풀이를 적용하기에는 2^15*2^15 크기의 메모리를 사용해야 하기 때문에
    메모리 크기에 대한 이슈가 발행한다.
    
2.  따라서, 배열에 기록하는 과정 자체를 없애고 해당 좌표에 기록할 차례에 바로 출력하는 방법을
    택하게 되었는데 0.5초 시간 제한으로 시간 내에 통과하기 어렵다.
    
3.  시간을 줄이기 위해서는, 4가지의 사분면을 재귀로 일일히 탐색하는 과정 자체를
    가지치기하여 건너뛰어야 할 필요성이 있다.
    사분면 하나를 건너뛰어야할 때 해당 재귀 단계에서 주어지는 길이의 반의 제곱만큼
    수가 기록될 것이다. 따라서, 4, 1, 3, 2사분면 순서대로 skip할 수 있도록 범위를 좁혀
    계산했다.
"""

import sys

N, R, C = map(int, input().split())

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]

count = 0


def write(length, x, y):
    global count
    if length == 2:
        for i in range(4):
            if x + dx[i] == R and y + dy[i] == C:
                print(count)
                sys.exit()
            count += 1
        return
    else:
        dir = -1
        if R < x + length // 2:
            if C < y + length // 2:
                dir = 0
            else:
                dir = 1
                count += (length // 2) ** 2
        else:
            if C < y + length // 2:
                dir = 2
                count += (length // 2) ** 2 * 2
            else:
                dir = 3
                count += (length // 2) ** 2 * 3
        write(length // 2, x + dx[dir] * length // 2, y + dy[dir] * length // 2)
    return


write(2 ** N, 0, 0)
