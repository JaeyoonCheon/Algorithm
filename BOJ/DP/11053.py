"""
11053번 가장 긴 증가하는 부분 수열

1.  DP
    가장 긴 증가하는 부분 수열에서 가장 중요한 것은 단위를 증가하는 부분 수열로 생각하는 것
    DP에 사용될 단위는 해당 수가 선택되었을 때, 앞에서부터 그 수 까지를 포함하여 만들 수 있는
    가장 긴 증가하는 부분 수열의 길이를 선택했다.
    따라서, bottom-up으로 각각의 가장 긴 증가하는 부분 수열의 길이를 저장하고, 그 길이는 이전에 저장된
    정보 중 수열 대소비교 후 선택한 수가 크다면 저장된 값에 +1을 한 후 그 값을 저장하면 된다.
"""

N = int(input())
A = list(map(int, input().split()))

cache = [0] * 1000
cache[0] = 1

for i in range(N):
    maxVal = 0
    for j in range(i):
        if A[i] > A[j]:
            if maxVal < cache[j]:
                maxVal = cache[j]
        cache[i] = maxVal + 1

print(max(cache))
