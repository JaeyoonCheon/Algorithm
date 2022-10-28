"""
3020번 개똥벌레

1.  처음 시도에서는 길이 i에서 각 높이 j마다 존재하는 장애물이 있는 지 없는 지 체크해 이전 위치의 해당 높이에서의 값에 1을 더해 장애물의 위치를 파악.
    하지만 어떻게 최적화를 해보아도 시간초과가 났는데 당연하게도 200000*500000의 칸을 검사하는것과 마찬가지이므로 시간초과가 발생할 수 밖에 없다.
    
2.  DP에서 시간을 최적화하기 위한 대표적인 방법으로 누적 합을 이용한 방식과 이분탐색을 이용해 NM을 logNM으로 줄이는 방식이 있는데 누적 합을 이용하는
    방식으로 접근했다.
    
3.  loop를 한번만 진행하기 위해 각 위치에서 주어지는 종유석/석순의 높이로만 총 높이 별 장애물 카운트를 셀 수 있도록 구성한다.
    종유석/석순 별도로 각 높이 별 종유석/석순의 총 개수를 더해놓은 뒤, 가장 높은 높이에서부터 내려오면 해당 높이에서의 통과해야 하는 장애물의
    개수를 누적 합 방식으로 구할 수 있다고 하겠다.
"""
import sys

N, H = map(int, sys.stdin.readline().split())

land = [0] * (H + 1)
roof = [0] * (H + 1)

isOdd = True

for _ in range(N):
    size = int(sys.stdin.readline())

    if isOdd:
        land[size] += 1
    else:
        roof[size] += 1

    isOdd = not isOdd

for i in range(H - 1, 0, -1):
    land[i] += land[i + 1]
    roof[i] += roof[i + 1]

land.pop(0)
roof.pop(0)

roof.reverse()

dp = list(map(lambda x, y: x + y, land, roof))

minCount = [float("inf"), 0]

for i in range(H):
    if dp[i] < minCount[0]:
        minCount[0] = dp[i]
        minCount[1] = 0
        minCount[1] += 1
    elif dp[i] == minCount[0]:
        minCount[1] += 1
    else:
        continue

print(f"{minCount[0]} {minCount[1]}")
