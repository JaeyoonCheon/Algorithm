"""
14002번 가장 긴 증가하는 부분 수열 4

1.  11053 가장 긴 증가하는 부분 수열 문제의 변형
    해당 문제에서 부분 수열의 길이만 구했다면 이번 문제에서는 그 수열을 출력해야 한다.

2.  각 부분 수열의 최대 길이를 구하는 순간에 사용되는 이전의 최대 길이 정보를 가진 수의 인덱스를 저장하는
    방식으로 방향을 정했다.
    cache[-][0]은 앞에서부터 그 수를 포함해 만들 수 있는 가장 긴 증가하는 부분 수열의 길이,
    cache[-][1]은 그 수 이전의 기장 값이 큰 수의 인덱스 정보를 저장하였다.
    이후 cache[-][0] 중 가장 큰 것을 최대 길이로 간주하고 그 최대 길이가 위치하는 인덱스의 cache[-][1]부터
    반대로 따라 지나가면서 수열을 저장, 반전하면 최장 증가 부분 수열을 출력할 수 있다.
"""

N = int(input())

A = list(map(int, input().split()))

cache = [[0, -1] for _ in range(1000)]
cache[0][0] = 1

for i in range(N):
    maxVal = 0
    maxIdx = -1
    for j in range(i):
        if A[i] > A[j]:
            if maxVal < cache[j][0]:
                maxVal = cache[j][0]
                maxIdx = j
        cache[i][0] = maxVal + 1
        cache[i][1] = maxIdx

length = max(c[0] for c in cache)

print(length)

start = -1
for i, v in enumerate(cache):
    if v[0] == length:
        start = i
        break

seq = []

for i in range(length):
    if cache[start][1] == -1:
        seq.append(A[start])
        break
    seq.append(A[start])
    start = cache[start][1]

seq.reverse()

for i in seq:
    print(i, end=" ")
