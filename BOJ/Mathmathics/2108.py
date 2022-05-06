"""
2108번 통계학

1.  주어지는 N개의 수에 대해 산술평균, 중앙값, 범위를 구하는 것은 어렵지 않다.

2.  최빈값은 단순히 주어진 N개의 수가 저장된 리스트에서 가장 많이 나타나는 수들을 찾고
    여러 개의 동일한 빈도의 최빈값이 있을 경우 두번째로 작은 값을 출력해야 하는데
    기본 파이썬 메소드 count를 사용하여 위의 작업을 수행하면 500000개의 수에서
    한번 시행될 때 마다 500000개를 모두 찾아야 하므로 2초 시간제한 내에 풀이해 내기 힘들다.
    
3.  따라서, N개 수를 입력받는 순간 값을 저장하는 lists 리스트와 별개로 그 수가
    몇 번 나타나는 지를 체크하는 counts 리스트를 만들어 쉽게 최빈값을 찾을 수 있다.
"""

import sys

N = int(sys.stdin.readline())

lists = []
counts = [0] * 8002

for _ in range(N):
    value = int(sys.stdin.readline())
    lists.append(value)
    counts[value + 4000] += 1

lists.sort()

print(round(sum(lists) / N))
print(lists[N // 2])

mode = max(counts)
isMultiple = counts.count(mode)
ONEORMORE = 1
if isMultiple > 1:
    ONEORMORE = 2
radix = 0

for i, v in enumerate(counts):
    if v == mode:
        radix += 1
        if radix == ONEORMORE:
            print(i - 4000)

print(max(lists) - min(lists))
