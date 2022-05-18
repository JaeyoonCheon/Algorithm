"""
2630번 색종이 만들기

1.  기본적인 재귀-분할정복 문제.

2.  정사각형을 N인 길이에서 모두 파란색/흰색인 지 검사하고 맞다면 해당 색의 개수를 증가,
    모두 같은 색이 아니라면 4개의 사분면으로 나누어 N/2의 길이에서 동일한 4분의 검사를 수행
"""

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

blue = 0
white = 0


def check(x, y, N):
    global blue, white

    thisColor = paper[x][y]
    isSame = True

    for i in range(x, x + N):
        for j in range(y, y + N):
            if paper[i][j] != thisColor:
                isSame = False

    if isSame:
        if thisColor == 0:
            white += 1
        else:
            blue += 1
    else:
        check(x, y, N // 2)
        check(x, y + N // 2, N // 2)
        check(x + N // 2, y, N // 2)
        check(x + N // 2, y + N // 2, N // 2)


check(0, 0, N)

print(white)
print(blue)
