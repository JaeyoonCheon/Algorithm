"""
    lv.2 교점에 별 만들기
    
    1.  문제에서 주어지는 예시대로 순서를 지키면서 풀이
    2.  풀이 순서
        1)  교점 구하기 & 최대 최소 좌표 구하기
        2)  .으로 초기화된 좌표계에 최소값만큼 평행이동한 교점들을 *로 대치
        3)  해당 좌표계를 표현한 배열을 x축 기준 반전(배열에서의 인덱스 축 반전 필요)
"""


def solution(line):
    n = len(line)
    points = []
    minX = minY = int(1e15)
    maxX = maxY = -int(1e15)

    for i in range(n):
        a, b, e = line[i]
        for j in range(i + 1, n):
            c, d, f = line[j]

            if a * d == b * c:
                continue

            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)

            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)

                points.append([x, y])

                if minX > x:
                    minX = x
                if minY > y:
                    minY = y
                if maxX < x:
                    maxX = x
                if maxY < y:
                    maxY = y

    lenX, lenY = maxX + 1 - minX, maxY + 1 - minY
    temp = [["."] * lenX for _ in range(lenY)]

    for point in points:
        x, y = point

        nx = x + abs(minX) if minX < 0 else x - minX
        ny = y + abs(minY) if minY < 0 else y - minY

        temp[ny][nx] = "*"

    answer = []

    for i in range(len(temp) - 1, -1, -1):
        answer.append("".join(temp[i]))

    return answer


line = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]

print(solution(line))
