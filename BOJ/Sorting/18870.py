"""
18870번 좌표 압축

1.  주어진 임의의 좌표들을 0부터 상대적인 크기로 1씩 차이나도록 좌표를 압축시키는 문제.

2.  처음 시도에서는 check함수에서 딕셔너리에 입력된 값을 넣을 때 상대적 순위를 모든 딕셔너리
    아이템들에 대해 매겨주고 갱신함으로써 최종적으로 딕셔너리에 해당 값:순위를 가지도록 구현했으나
    갱신 시 딕셔너리의 모든 개체에 대해 순회해야 하므로 O(N)시간이 들어 시간 내에 풀기 힘들었다.
    
3.  우리가 찾고자 하는 것은 각 좌표들의 상대적! 위치이므로, 중복을 제거한 좌표들을(Set 이용)
    오름차순 정렬하고 그 인덱스를 값으로 가지는 딕셔너리를 별도의 갱신 과정이 필요 없도록 구현하였다.
"""

import sys

N = int(input())

pos = {}


def check(num):
    num = int(num)
    radix = 0
    if num in pos.keys():
        return
    else:
        for k, v in pos.items():
            if num > k:
                radix += 1
            elif num < k:
                pos[k] += 1

        pos[num] = radix


inputs = list(map(int, sys.stdin.readline().split()))
toSet = set(inputs)
sortedSet = sorted(toSet)
toDict = {key: value for value, key in enumerate(sortedSet)}

for i in inputs:
    print(toDict[i], end=" ")
