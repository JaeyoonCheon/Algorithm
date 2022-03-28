"""
11052번 카드 구매하기

1.  DP문제 중 생각을 해야했던 문제

2.  N개를 사야하는데 이전의 구매내역 중 최대값 정보를 사용하는 문제
    만약, 4개를 사는 문제라면 몇가지 경우를 생각해 볼 수 있다.
    1) 1개짜리 카드팩을 사고 나머지 3개를 최대가격으로 구매
    2) 2개짜리 카드팩을 사고 나머지 2개를 최대가격으로 구매
    3) 3개짜리 카드팩을 사고 나머지 1개를 최대가격으로 구매
    4) 4개짜리 카드팩을 사고 나머지 0개를 최대가격으로 구매
    (0개짜리 카드팩을 사는 경우는 존재할 수 없다. 무한반복)
    
    이 4가지 경우 중 최대값을 선택하여 저장하고 다시 그 정보를 N개를 구하는데 사용
"""

N = int(input())
P = list(map(int, input().split()))
P.insert(0, 0)
cache = [0] * 1001

for i in range(1, N + 1):
    for j in range(1, i + 1):
        cache[i] = max(cache[i], cache[i - j] + P[j])

print(cache[N])