"""
11651번 좌표 정렬하기 2

1.  이중 키 값 정렬 문제
"""

N = int(input())

coordinate = [list(map(int, input().split())) for _ in range(N)]

sortedCoordinate = sorted(coordinate, key=lambda k: (k[1], k[0]))

for i in sortedCoordinate:
    print(f"{i[0]} {i[1]}")
