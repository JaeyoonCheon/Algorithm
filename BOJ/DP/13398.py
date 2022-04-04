"""
13398번 연속합 2
"""

n = int(input())

A = list(map(int, input().split()))

cache = [[-1001, -1001] for _ in range(n)]
cache[0][0] = A[0]

for i in range(1, n):
    cache[i][0] = max(cache[i - 1][0] + A[i], cache[i - 1][1] + A[i], A[i])
    if i == n - 1:
        cache[i][1] = cache[i - 1][1]
    else:
        cache[i][1] = max(cache[i - 1][1] + A[i + 1], A[i + 1])

max = -1001
for i in range(n):
    for j in range(2):
        if max < cache[i][j]:
            max = cache[i][j]

print(max)
