"""
1932번 정수 삼각형

1.  부분 단위는 해당 수를 선택했을 때 가장 위쪽부터 내려오는 경로의 최대 합

2.  선택할 수 있는 경우는 3가지로,
    1)  일반적인 경우 자신의 바로 위쪽과 좌상위 수의 대소 비교
    2)  가장 왼쪽 수의 경우 자신의 바로 위쪽만 선택
    3)  가장 오른쪽 수의 경우 좌상위 수만 선택
"""

N = int(input())

case = []

for i in range(N):
    case.append(list(map(int, input().split())))

cache = []

for i in range(N):
    cache.append([0] * (i + 1))

cache[0][0] = case[0][0]

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            cache[i][j] = cache[i - 1][j] + case[i][j]
        elif j == i:
            cache[i][j] = cache[i - 1][j - 1] + case[i][j]
        else:
            cache[i][j] = max(cache[i - 1][j - 1], cache[i - 1][j]) + case[i][j]

print(max(cache[N - 1]))
