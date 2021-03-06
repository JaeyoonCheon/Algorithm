"""
1912번 연속합

1.  연속합
    연속합이라는 것은 연속된 숫자들의 합을 구하는 것으로, 이 때의 수열에는 음수 또한 포합되어 있으므로
    현재 선택한 수를 지금까지의 연속된 숫자들의 합에 더한다고 하여도 현재 선택한 수보다 작아질 수 있다.
    현재 수를 더한 순간 작아진다고 생각하면, 그 부분에서 최대 연속합은 깨지게 된다.
    따라서 각 수에 저장되는 정보는 지금까지의 최대 연속합으로, 이전 연속합에 자기 자신을 더한 것과
    이전 합이 현재 수보다 작아 현재 수부터 다시 연속합을 고려하는 것이 큰 지 비교하는 식이 점화식이 된다.
    결국 점화식은 cache[n] = max(A[n], cache[n-1] + A[n])이 된다.
"""

N = int(input())

A = list(map(int, input().split()))

cache = [0] * N
cache[0] = A[0]

for i in range(1, N):
    cache[i] = max(A[i], cache[i - 1] + A[i])

print(max(cache))
