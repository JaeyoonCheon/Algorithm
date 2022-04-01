"""
11722번 가장 긴 감소하는 부분 수열

1.  최대 수열이 아닌 최장 수열

2.  부분 단위 cache[i]는 해당 수를 선택했을 때의 만들 수 있는 감소 수열의 최장 길이

3.  이전 값이 현재 값보다 작은 경우를 모두 제하고,
    선택할 수 있는 이전 값 중에 저장된 부분 단위 + 1이 가장 큰 것을 선택하여 N까지 기록
"""

N = int(input())

A = list(map(int, input().split()))

cache = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] >= A[j]:
            continue
        if cache[j] + 1 > cache[i]:
            cache[i] = cache[j] + 1

print(max(cache))
