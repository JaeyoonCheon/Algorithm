"""
1149번 RGB거리

1.  이 문제에서 사용할 수 있는 부분 단위는 어떤 집 i를 각각 빨강, 초록, 파랑으로 칠할 수 있는 최소 비용이다.
    따라서, cache[i][0], cache[i][1], cache[i][2]를 i를 빨강, 초록, 파랑으로 칠할 수 있는 최소 비용으로
    설정해 놓고 bottom-up으로 구성하였다.
    
2.  기저조건은 가장 첫 집은 주어지는 비용과 동일하다는 것

3.  두번쨰 집 부터
    1)  빨강일 때 이전의 집이 초록/파랑 집만 가능하다.
        따라서 이전 집의 초록/파랑 집 중 누적 합이 최소인 것 + 선택한 빨강 집의 비용
    2)  초록일 때 이전의 집이 빨강/파랑 집만 가능하다.
        따라서 이전 집의 빨강/파랑 집 중 누적 합이 최소인 것 + 선택한 초록 집의 비용
    3)  파랑일 때 이전의 집이 빨강/초록 집만 가능하다.
        따라서 이전 집의 빨강/초록 집 중 누적 합이 최소인 것 + 선택한 파랑 집의 비용
        
4.  이후 N번째 집의 누적 비용까지 계산한 후 그것의 최소를 결정
"""

N = int(input())

cost = [list(map(int, input().split())) for _ in range(N)]
cost.insert(0, [0, 0, 0])

cache = [[0, 0, 0] for _ in range(N + 1)]

for i in range(3):
    cache[1][i] = cost[1][i]

for i in range(2, N + 1):
    cache[i][0] = min(cache[i - 1][1], cache[i - 1][2]) + cost[i][0]
    cache[i][1] = min(cache[i - 1][0], cache[i - 1][2]) + cost[i][1]
    cache[i][2] = min(cache[i - 1][0], cache[i - 1][1]) + cost[i][2]

print(min(cache[N]))
