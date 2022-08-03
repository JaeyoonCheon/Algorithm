"""
2467번 용액

1.  백만개의 용액들 중 단 2개만을 선택해 합쳐 0이 가까운 용액을 만들어야 하므로
    O(N) 시간복잡도를 가지는 알고리즘은 비효율적이 될 것이고 따라서 O(logN) 시간복잡도의
    이분 탐색이나 투 포인터 알고리즘을 채택하는 것이 합리적이다.

2.  이번 풀이에서는 투 포인터 방법을 사용하여 양 끝에서부터 검사하면서 범위를 좁히는데
    합의 절대값이 최소가 되는 지점을 저장하도록 한다.
    또한 두 용액의 합이 0보다 작다면 더해야 하므로 왼쪽 포인터를 1 증가시키고
    0보다 크다면 빼야 하므로 오른쪽 포인터를 1 감소시켜 동작하도록 한다.
"""

import sys

N = int(input())

fluids = list(map(int, sys.stdin.readline().split()))

left = 0
right = len(fluids) - 1

minDet = float("inf")
minFluid = []

while left < right and minDet != 0:
    det = abs(fluids[right] + fluids[left])
    if det < minDet:
        minDet = det
        minFluid = [fluids[left], fluids[right]]

    if fluids[right] + fluids[left] < 0:
        left += 1
    else:
        right -= 1

print(f"{minFluid[0]} {minFluid[1]}")
