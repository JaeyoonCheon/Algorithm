"""
16566번 카드 게임

1.  문제의 풀이는 문제에서 제시한 대로 구현하여 제시된 카드보다 큰 카드가 내 덱에 있을 경우
    그 중 가장 작은 카드를 내고, 없을 때 가진 카드 중 가장 작은 것을 낸다.
    
2.  시간을 줄이는 테크닉으로 2가지가 있다.
    1)  이분 탐색 upper-bound
        내 덱을 정렬한 뒤 upper-bound를 사용하면 제시된 카드보다 큰 카드 중 가장 작은 것을 구할 수 있다.
    2)  서로소 집합의 응용
        한번 제시되어 낸 카드는 버려져야 하는데, 철수는 냈던 카드를 또 낼 수 있으므로
        해당 제시된 카드에 대해 버린 카드 그 이상을 내야 한다. 따라서, 버릴 떄 다음 카드를 root에 등록시켜(union) 놓으면
        버린 카드를 골랐을 떄 그 다음으로 큰 카드를 선택할 수 있다.
        이 때, 현재 카드가 끝(가장 큰 경우)라면 union을 하지 않는다.
"""

import sys, copy, collections, bisect

N, M, K = map(int, sys.stdin.readline().split())

selectedCards = list(map(int, sys.stdin.readline().split()))
selectedCards.sort()

chul = list(map(int, sys.stdin.readline().split()))

root = [x for x in range(M)]


def find(v):
    if v == root[v]:
        return v
    v = find(root[v])
    root[v] = v
    return v


def union(a, b):
    if b == M:
        return

    a = find(a)
    b = find(b)
    root[a] = b


def biSelection_upper(idx):
    start, end = 0, M

    while start < end:
        mid = (start + end) // 2

        if selectedCards[mid] > idx:
            end = mid
        else:
            start = mid + 1

    return end


for cur in chul:
    next = biSelection_upper(cur)
    next = find(next)

    print(selectedCards[next])

    union(next, next + 1)
