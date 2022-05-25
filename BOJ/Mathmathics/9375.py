"""
9375번 패션왕 신해빈

1.  주어진 카테고리에 속하는 의상들을 중복없이 1개 이상 입는 공집합을 제외한 중복조합을 결정하는 문제.

2.  각 카테고리에 속하는 의상의 개수는 딕셔너리를 이용해 카운트하고,
    계산된 의상들의 수로 중복조합 - 1을 계산한다.
"""

T = int(input())

for _ in range(T):
    N = int(input())

    if N == 0:
        print(0)
        continue

    clothes = {}

    for _ in range(N):
        name, category = input().split()

        if not category in clothes.keys():
            clothes[category] = 1
        else:
            clothes[category] += 1

    comb = 1

    for key, value in clothes.items():
        comb *= value + 1
    comb -= 1

    print(comb)
