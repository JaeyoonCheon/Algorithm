"""
11054번 가장 긴 바이토닉 부분 수열

1.  가장 긴 증가 부분 수열 + 가장 긴 감수 부분 수열 문제

2.  양 방향에서 가장 긴 증가 부분 수열을 계산한 후 해당하는 인덱스에서 가장 큰 길이의 합을 가지는
    위치를 찾는다.
"""

N = int(input())

A = list(map(int, input().split()))

cache = [[1, 1] for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if A[i] <= A[j]:
            continue
        cache[i][0] = max(cache[j][0] + 1, cache[i][0])

for i in range(N - 1, -1, -1):
    for j in range(i + 1, N):
        if A[i] <= A[j]:
            continue
        cache[i][1] = max(cache[j][1] + 1, cache[i][1])

maxLength = 0

for i in cache:
    if sum(i) > maxLength:
        maxLength = sum(i)

print(maxLength - 1)
