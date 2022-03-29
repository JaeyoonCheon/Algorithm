"""
15988번 1, 2, 3 더하기 3

1.  cache[i]는 정수 i에 대해 1, 2, 3으로 만들 수 있는 중복을 허용하고 순서를 구분하는 모든 경우의 수

2.  정수 1, 2, 3인 기저 조건을 설정해 놓고 4부터 요구하는 가장 큰 수까지 올라가면서
    해당 수에서 1을 뺀 수의 경우 + 2를 뺀 수의 경우 + 3을 뺀 수의 경우를 모두 더하면
    해당 수에서 가질 수 있는 모든 경우의 수를 구할 수 있다
"""

T = int(input())

case = []

for _ in range(T):
    case.append(int(input()))

length = max(case)

cache = [0] * (length + 1)

cache[1] = 1
cache[2] = 2
cache[3] = 4

for i in range(4, length + 1):
    cache[i] = (cache[i - 1] + cache[i - 2] + cache[i - 3]) % 1000000009

for i in case:
    print(cache[i] % 1000000009)

"""
1 -> : 1
2 -> 1+1 2 : 2
3 -> 1+1+1 1+2 2+1 3: 4
"""
