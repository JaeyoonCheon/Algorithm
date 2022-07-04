"""
15663번 N과 M(9)

1.  N개 수 중 M개를 뽑아 순서가 있고 중복이 없는 순열을 만드는 문제.

2.  도중 permutation 값이 저장된 list가 set으로 변환되지 않은 문제가 있었으나
    새 객체에 값을 부여하여 처리하였더니 정상동작
"""

import copy, itertools

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

perm = list(itertools.permutations(numbers, M))

uniquePerm = set(perm)
uniquePerm = sorted(uniquePerm)

for i in uniquePerm:
    for j in i:
        print(j, end=" ")
    print()
