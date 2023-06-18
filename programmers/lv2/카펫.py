"""
    lv.2 카펫
    
    1.  가로 x 세로 로 성립 가능한 모든 조합에 대해 탐색.
    2.  해당 조합에 대해, 외곽을 잘라낸 넓이가 yellow와 동일하면 탐색 종료.
"""


def solution(brown, yellow):
    answer = []

    total = brown + yellow

    for col in range(3, int(total**0.5) + 1):
        if total % col != 0:
            continue

        row = total // col

        if (row - 2) * (col - 2) == yellow:
            answer = [row, col]
            break

    return answer
