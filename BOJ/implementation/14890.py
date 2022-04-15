"""
14980번 경사로

1.  지도 + 경로 구현 문제

2.  같은 행/열에 대해 그 행/열을 1자로 지나갈 수 있으면 '길'이라고 정의
    지나가는 칸들의 높이가 같다면 지나갈 수 있으며, 1칸 차이가 날 때는 경사로를 놓아 지나갈 수 있다.
    
3.  경사로
    1칸 차이가 날 때 놓을 수 있는 조건으로, 무조건 L길이의 경사로이고 경사로가 놓이는 곳은 높이가 같아야 한다.
    이를 위해, 수평/수직에서 오르막/내리막을 구현
    
4.  gradient배열
    이미 경사로가 놓인 곳을 파악하기 위해 만든 배열.
    가로인 길을 탐색한 후 세로인 길을 탐색하기 위해 초기화 필수
"""

N, L = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

gradient = [[0] * N for _ in range(N)]

gradientNumber = 1
count = 0

# x, y는 높이가 변하는 대상 지점
def checkGradient(x, y, type):
    global gradientNumber
    if type == "horizontal-incline":
        if y >= L:
            start = maps[x][y - L]
            for i in range(y - L, y):
                if gradient[x][i] != 0 or start != maps[x][i]:
                    return False
                gradient[x][i] = gradientNumber
            gradientNumber += 1
            return True
        else:
            return False
    elif type == "horizontal-decline":
        if N - y >= L:
            start = maps[x][y]
            for i in range(y, y + L):
                if gradient[x][i] != 0 or start != maps[x][i]:
                    return False
                gradient[x][i] = gradientNumber
            gradientNumber += 1
            return True
        else:
            return False
    elif type == "vertical-incline":
        if x >= L:
            start = maps[x - L][y]
            for i in range(x - L, x):
                if gradient[i][y] != 0 or start != maps[i][y]:
                    return False
                gradient[i][y] = gradientNumber
            gradientNumber += 1
            return True
        else:
            return False
    else:
        if N - x >= L:
            start = maps[x][y]
            for i in range(x, x + L):
                if gradient[i][y] != 0 or start != maps[i][y]:
                    return False
                gradient[i][y] = gradientNumber
            gradientNumber += 1
            return True
        else:
            return False


for i in range(N):
    flag = True
    for j in range(1, N):
        if maps[i][j - 1] - maps[i][j] == 1:
            if checkGradient(i, j, "horizontal-decline") == False:
                flag = False
                break
        elif maps[i][j - 1] - maps[i][j] == -1:
            if checkGradient(i, j, "horizontal-incline") == False:
                flag = False
                break
        elif maps[i][j - 1] == maps[i][j]:
            continue
        else:
            flag = False
            break
    if flag:
        count += 1

gradient = [[0] * N for _ in range(N)]

for i in range(N):
    flag = True
    for j in range(1, N):
        if maps[j - 1][i] - maps[j][i] == 1:
            if checkGradient(j, i, "vertical-decline") == False:
                flag = False
                break
        elif maps[j - 1][i] - maps[j][i] == -1:
            if checkGradient(j, i, "vertical-incline") == False:
                flag = False
                break
        elif maps[j - 1][i] == maps[j][i]:
            continue
        else:
            flag = False
            break
    if flag:
        count += 1

print(count)
