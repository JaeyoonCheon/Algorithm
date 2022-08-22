"""
1509번 팰린드롬 분할

1.  우선 주어진 문자열의 임의의 인덱스 [a,b]에 대한 모든 팰린드롬 여부를 구해놓도록 한다.

2.  이후 구해놓은 팰린드롬 여부의 정보를 가지고 [0,length(s)]에 대한 최소 팰린드롬 분할의 개수를 결정해야 한다.

3.  dp[x]는 0부터 x까지의 부분 문자열에서 나타나는 최소 팰린드롬 분할의 수이다.
    최소인 경우를 구해야 하므로 무한대로 초기화하며, dp[0]은 0이 된다.
    
4.  이때, 모든 부분 문자열을 순회하면서 해당 구간 [START,END]가 팰린드롬인지 아닌지에 따라 행동하는 방식이 달라진다.
    1)  해당 구간이 팰린드롬일 경우
        해당 구간 전체를 하나의 팰린드롬으로 생각하는 것이 최소치일 것이므로, [0, END]는 [0,START]의 dp값에다 하나의 팰린드롬을 더한 경우와
        이전에 계산된 dp[END]와 비교하여 더 작은 값을 선택하는 것이 바람직하다.
        dp[END] = min(dp[END], dp[START - 1] + 1)
    2)  해당 구간이 팰린드롬이 아닌 경우
        해당 구간은 팰린드롬이 아니므로, END-1까지의 구간에 길이 1짜리 문자가 덧붙여져 팰린드롬이 성립하지 않는 경우로 간주한다.
        해당 경우와 이전에 계산된 dp[END]를 서로 비교해 더 작은 값을 선택한다.
        dp[END] = min(dp[END], dp[END - 1] + 1)
"""

s = list(input().rstrip())

length = len(s)

palindrom = [[False] * length for _ in range(length)]

for i in range(length):
    palindrom[i][i] = 1

for i in range(1, length):
    if s[i] == s[i - 1]:
        palindrom[i - 1][i] = True

for i in range(3, length + 1):
    for start in range(length - i + 1):
        end = start + i - 1

        if s[start] == s[end]:
            if palindrom[start + 1][end - 1]:
                palindrom[start][end] = True

dp = [float("inf")] * (length + 1)
dp[-1] = 0

for _to in range(length):
    for _from in range(_to + 1):
        if palindrom[_from][_to]:
            dp[_to] = min(dp[_to], dp[_from - 1] + 1)
        else:
            dp[_to] = min(dp[_to], dp[_to - 1] + 1)

print(dp[length - 1])
