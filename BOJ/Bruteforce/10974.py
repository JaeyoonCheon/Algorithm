"""
10974번 모든 순열

1. 파이썬의 itertools.permutations 메소드 이용
    itertools의 permutations메소드는 첫번째 인자로 수의 범위, 두번째 인자로 뽑을 갯수를 받아
    조건 하에서 만들어 낼 수 있는 모든 순열을 만들어 낸다.
    
2. 재귀
    백트래킹을 이용한 1 ~ N 범위 내의 모든 원소에 대한 재귀를 종료조건 length == N으로 설정하여 수행.
    itertools의 메소드보다는 최적화가 부족하나 준수한 성능
"""

import itertools

N = int(input())


def iterator(N):
    for i in itertools.permutations(range(1, N + 1), N):
        for j in i:
            print(j, end=" ")
        print("")


def recursiveIter(N, length, bin):
    if length == N:
        for j in bin:
            print(j, end=" ")
        print("")
        return

    for i in range(1, N + 1):
        if i in bin:
            continue

        bin.append(i)
        recursiveIter(N, length + 1, bin)
        bin.pop()


# iterator(N)

bin = []
recursiveIter(N, 0, bin)
