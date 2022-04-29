"""
2798번 블랙잭

1.  1장이 아닌 선택한 3장의 합이 21을 넘지 않는 범위에서 가장 가까우면 이기도록 조건이 주어짐

2.  범위가 그렇게 크지 않으므로, 완전탐색으로 3장의 카드를 중복없이 뽑아 정대값을 비교
"""

N, M = map(int, input().split())

cards = list(map(int, input().split()))

nearest = 0
diff = M

for i in range(N):
    for j in range(N):
        if j == i:
            continue
        for k in range(N):
            if k == i or k == j:
                continue
            summation = cards[i] + cards[j] + cards[k]
            if summation <= M and diff > abs(M - summation):
                diff = abs(M - summation)
                nearest = summation

print(nearest)
