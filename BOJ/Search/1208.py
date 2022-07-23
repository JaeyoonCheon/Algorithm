"""
1208번 부분수열의 합 2

1.  부분수열의 합 1 문제와는 다르게 수열의 개수가 40개이고
    완전탐색으로 모든 부분수열을 구하려면 O(2^N)이므로 최악의 경우 2^40이 소요된다.

2.  부분수열의 조합 자체는 구해야 하지만 경과되는 시간을 줄이기 위해
    우선 주어지는 수열 자체를 반으로 쪼개 각각 연산하는 것이다.
    반으로 쪼개진 수열에 대해 부분수열의 조합을 계산해 저장해 놓고,
    그 두 결과의 원소 각각에 대해서, 더해서 S가 되는 경우를 증가시키면 된다.

3.  더해서 S가 되는 경우를 계산하기 위해 투포인터로 접근하려고 했으나,
    인덱스 조건을 잘못 주어 로직을 짜기가 어려웠기 때문에
    이진탐색의 upper bound - lower bound를 응용해 가능한 경우의 수를 찾았다.
    추후 투 포인터 방법도 수정해 동작하도록 할 예정이다.
"""

import sys, itertools, bisect

N, S = map(int, input().split())

seq = list(map(int, sys.stdin.readline().split()))

seq_head, seq_tail = seq[: len(seq) // 2], seq[len(seq) // 2 :]

comb_head, comb_tail = [], []

for i in range(len(seq_head) + 1):
    combination = list(itertools.combinations(seq_head, i))
    comb_head.extend(combination)

for i in range(len(seq_tail) + 1):
    combination = list(itertools.combinations(seq_tail, i))
    comb_tail.extend(combination)

sum_comb_head = sorted(list(map(sum, comb_head)))
sum_comb_tail = sorted(list(map(sum, comb_tail)))


def twoPointer():
    head, tail = 0, len(sum_comb_tail) - 1

    count = 0
    if S == 0:
        count -= 1

    while head < len(sum_comb_head) - 1 or tail > 0:
        if sum_comb_head[head] + sum_comb_tail[tail] == S:
            count_head = 1
            while head < len(sum_comb_head) - 1 and sum_comb_head[head] == sum_comb_head[head + 1]:
                head += 1
                count_head += 1

            count_tail = 1
            while tail > 0 and sum_comb_tail[tail] == sum_comb_tail[tail - 1]:
                tail -= 1
                count_tail += 1

            count += count_head * count_tail
            if head < len(sum_comb_head) - 1:
                head += 1
            else:
                if tail > 0:
                    tail -= 1
                else:
                    head += 1
                    tail -= 1
        elif sum_comb_head[head] + sum_comb_tail[tail] > S:
            tail -= 1
        else:
            head += 1

    if head == len(sum_comb_head) - 1 and tail == 0:
        if sum_comb_head[head] + sum_comb_tail[tail] == S:
            count += 1

    print(count)


def binarySearch():
    count = 0

    for i in range(len(sum_comb_head)):
        curr = sum_comb_head[i]

        upper = bisect.bisect_left(sum_comb_tail, S - curr)
        lower = bisect.bisect_right(sum_comb_tail, S - curr)

        count += abs(upper - lower)

    if S == 0:
        count -= 1

    print(count)


binarySearch()
