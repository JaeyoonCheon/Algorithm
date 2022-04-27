"""
1978번 소수 찾기

1.  1001 범위 내의 자연수들에 대해 에라토스테네스의 체 적용
"""

N = int(input())

numbers = [True] * 1001
numbers[0] = numbers[1] = False

for i in range(2, 1001):
    if i == False:
        continue
    j = 2
    while i * j <= 1000:
        numbers[i * j] = False
        j += 1


lists = list(map(int, input().split()))

count = 0

for i in lists:
    if numbers[i]:
        count += 1

print(count)
