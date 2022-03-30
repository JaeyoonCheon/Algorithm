"""
2156번 포도주 시식

1.  일반적인 DP문제에 3잔 연속 선택하지 말라는 조건이 붙은 문제
    부분 단위 cache[i]는 어떤 잔 i를 선택했을 때 그 앞에 놓인 잔까지 합쳐 먹는 최대 양
    
2.  어떤 잔 i를 선택했다고 했을 때, 부분 단위 cache[i]가 결정되는 케이스는 3가지이다.
    1) 2번째 전 잔을 선택하는 경우
    2-1) 1번째 전 잔과 그로부터 2번째 전 잔(현재 기준 3번째 전 잔)을 선택하는 경우
    2-2) 1번째 전 잔과 그로부터 3번째 전 잔(현재 기준 4번째 전 잔)을 선택하는 경우
"""

n = int(input())

case = [int(input()) for _ in range(n)]
cache = [0] * n

cache[0] = case[0]

if n > 1:
    cache[1] = case[0] + case[1]

if n > 2:
    cache[2] = max(case[0], case[1]) + case[2]

for i in range(3, n):
    cache[i] = case[i] + max(
        cache[i - 2], cache[i - 3] + case[i - 1], cache[i - 4] + case[i - 1]
    )

print(max(cache))
