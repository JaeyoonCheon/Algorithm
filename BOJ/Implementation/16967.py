"""
16967번 배열 복원하기

1.  겹친 부분 i - X >= 0 and j - Y >= 0
    이 범위는 배열이 이동해서 만들어지는 겹쳐진 부분의 두 수가 존재하는 경우를 의미
    
2.  따라서, 겹친 부분의 수에 계산된 원 배열의 수를 뻬주면 겹치기 전의 수가 계산됨
    이 떄, 원 배열의 수가 아닌 겹친 배열의 수를 빼주면 수가 변동되지 않아 잘못된 값이 도출
"""

H, W, X, Y = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(H + X)]
original = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        # i-X, j-Y는 겹쳐져서 차를 구해야 할 곳이 있는 지 체크
        if i - X >= 0 and j - Y >= 0:
            original[i][j] = maps[i][j] - original[i - X][j - Y]
        else:
            original[i][j] = maps[i][j]

for i in range(H):
    for j in range(W):
        print(original[i][j], end=" ")
    print()
