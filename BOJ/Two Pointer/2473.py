"""
2473번 세 용액

1.  2467번 용액 문제의 응용 버전이다.

2.  동일하게 투 포인터 방법으로 접근해봤는데, 포인터 3개를 움직이는 것은
    비효율적이라고 보아 세 용액 중 값이 중간이 되는 용액 하나는 고정시키고
    나머지 두 용액의 포인터만 양 쪽에서 움직이는 것으로 했다.

3.  중간 용액은 1 ~ len(fluids)-1 사이에 있는 용액 중 하나가 되며,
    나머지 두 용액은 0~중간용액-1, 중간용액+1~len(fluids) 사이에서 선택해
    투포인터로 범위를 좁혀가면서 가장 작은 합계를 이루는 조합을 찾는다.
"""

import sys

N = int(input())

fluids = list(map(int, sys.stdin.readline().split()))

minDet = float("inf")
minFluid = []

fluids.sort()

for mid in range(1, len(fluids) - 1):
    left = 0
    right = len(fluids) - 1

    while minDet != 0:
        det = abs(fluids[right] + fluids[mid] + fluids[left])
        if det < minDet:
            minDet = det
            minFluid = [fluids[left], fluids[mid], fluids[right]]

        if fluids[right] + fluids[mid] + fluids[left] < 0:
            if left == mid - 1:
                break
            left += 1
        else:
            if right == mid + 1:
                break
            right -= 1


print(f"{minFluid[0]} {minFluid[1]} {minFluid[2]}")
