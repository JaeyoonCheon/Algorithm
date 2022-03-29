"""
1309번 동물원

1.  2*N 크기의 동물 우리가 있다고 제시
    상태는 1)동물이 없거나 2)왼쪽 우리 3)오른쪽 우리에 있는 3가지가 있을 수 있다.
    
2.  각 우리는 인접한 우리와 동일한 위치에 동물을 위치시켜서는 안되므로,
    1)동물이 없을 경우 이전 우리에 위치하는 모든 경우의 수
    2)동물이 왼쪽에 있을 경우 이전 우리에 없거나 오른쪽에 위치한 모든 경우의 수
    3)동물이 오른쪽에 있을 경우 이전 우리에 없거나 왼쪽에 위치한 모든 경우의 수
    를 저장하여 마지막에 종합하면 총 경우의 수가 도출
"""

N = int(input())

cache = [[0, 0, 0] for i in range(N + 1)]

for i in range(3):
    cache[1][i] = 1

for i in range(2, N + 1):
    cache[i][0] = (cache[i - 1][0] + cache[i - 1][1] + cache[i - 1][2]) % 9901
    cache[i][1] = (cache[i - 1][0] + cache[i - 1][2]) % 9901
    cache[i][2] = (cache[i - 1][0] + cache[i - 1][1]) % 9901

print(sum(cache[N]) % 9901)