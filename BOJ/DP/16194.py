"""
16194번 카드 구매하기 2

1.  N개를 사야하는데 이전의 구매내역 중 최솟값 정보를 사용하는 문제
    만약, 4개를 사는 문제라면 몇가지 경우를 생각해 볼 수 있다.
    1) 1개짜리 카드팩을 사고 나머지 3개를 최소가격으로 구매
    2) 2개짜리 카드팩을 사고 나머지 2개를 최소가격으로 구매
    3) 3개짜리 카드팩을 사고 나머지 1개를 최소가격으로 구매
    4) 4개짜리 카드팩을 사고 나머지 0개를 최소가격으로 구매
    (0개짜리 카드팩을 사는 경우는 존재할 수 없다. 무한반복)
    
    이 4가지 경우 중 최소값을 선택하여 저장하고 다시 그 정보를 N개를 구하는데 사용
    
2.  11052번 카드 구매하기 문제와는 반대로 생각하고 풀어야 하는데
    최소값을 대조하여야 하므로 cache의 초기값을 크게 설정해 주어야하며
    cache[0]은 원 의미 상 0원이 되어야 하므로 0으로 설정해야 정확한 계산이 된다.
"""

N = int(input())
P = list(map(int, input().split()))
P.insert(0, 0)
cache = [10001] * 1000
cache.insert(0, 0)

for i in range(1, N + 1):
    for j in range(1, i + 1):
        cache[i] = min(cache[i], cache[i - j] + P[j])

print(cache[N])
