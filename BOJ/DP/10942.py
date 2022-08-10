"""
10942번 팰린드롬?

1.  다른 사람들의 풀이를 참고해서 푼 문제.

2.  dp를 사용하여 양 끝 start - end의 문자가 같을 떄 그 사이의
    start+1 ~ end-1의 dp 결과가 팰린드롬이라면 팰린드롬이라는 점화식 자체는
    생각했었으나, 주어지는 자연수가 100000범위 내의 수인데 정작 풀이 로직은
    자연수들이 한 자리 수이라는 것을 가정하고 푼다는 것이 이해되지 않는 문제.

3.  설명을 보고 이해한 바로는,
    주어지는 seq의 각 수가 '하나의 문자'라고 생각하여 풀이하는 것이다.
    만약, 123 100000 123으로 주이진다면, 1-3 쿼리의 결과는 양 끝 123 123이 동일하고
    내부가 길이 1인 팰린드롬(100000 자체가 1글자로 간주하자!)으로 팰린드롬으로 볼 수 있다는 것이다.
    처음 생각처럼 수들의 글자를 합쳐 문자열로 생각하는 문제가 아니었던 것이다.
"""

import sys

N = int(input())

dp = [[False] * N for _ in range(N)]

seq = list(map(int, sys.stdin.readline().split()))

for length in range(N):
    for s in range(N - length):
        e = s + length

        if s == e:
            dp[s][e] = True
        elif seq[s] == seq[e]:
            if s + 1 == e:
                dp[s][e] = True
            elif dp[s + 1][e - 1] == True:
                dp[s][e] = True

M = int(input())

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    if dp[start - 1][end - 1]:
        print(1)
    else:
        print(0)
