"""
    lv.3 정수 삼각형
    
    1.  높이를 내려오면서 점화식에 따라 누적 합을 저장하는 dp를 계산.
    2.  점화식을 매끄럽게 유지하기 위해, 0을 양 옆에 추가한 dp 배열을 선언해 사용.
"""


def solution(triangle):
    answer = 0

    height = len(triangle)
    sumTriangle = [[0, *v, 0] for v in triangle]

    for h in range(1, height):
        for j in range(1, h + 2):
            sumTriangle[h][j] = sumTriangle[h][j] + max(
                sumTriangle[h - 1][j - 1], sumTriangle[h - 1][j]
            )

    answer = max(sumTriangle[height - 1])

    return answer


result = solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
