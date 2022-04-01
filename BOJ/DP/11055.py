"""
11055번 가장 큰 증가 부분 수열

1.  부분 단위 cache[i]는 해당 수를 선택했을 때 만들 수 있는 해당 수 까지의 가장 큰 증가 부분 수열의 합

2.  해당 수에서 고려해야 할 부분은 지금까지 더해왔던 수열의 합과 현재 선택한 수 간 비교이다.
    선택한 수 이전의 모든 수의 부분 단위+현재 수 중 가장 큰 것을 선택
    
3.  계산된 모든 부분 단위 중 가장 큰 것이 가장 큰 증가 부분 수열의 최대합
"""

N = int(input())

case = list(map(int, input().split()))
cache = [0] * N

cache[0] = case[0]

for i in range(1, N):
    cache[i] = case[i]
    for j in range(i):
        if case[j] >= case[i]:
            continue
        cache[i] = max(cache[j] + case[i], cache[i])

print(max(cache))
