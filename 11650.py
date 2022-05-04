"""
11650번 좌표 정렬하기

1.  이중 정렬 문제.
    파이썬 기본 정렬 함수 sorted에 람다식으로 정렬 키를 2개 전달함으로서
    이중 정렬을 구현
"""

N = int(input())

pos = [list(map(int, input().split())) for _ in range(N)]

sortedPos = sorted(pos, key=lambda x: (x[0], x[1]))

for i in sortedPos:
    print(f"{i[0]} {i[1]}")
