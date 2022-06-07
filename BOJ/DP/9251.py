"""
9251번 LCS

1.  LCS?
    Longest Common Subsequence(최장 공통 부분 수열)
    
2.  두 문자열을 배열의 한 차원으로 생각하고 서로 비교하는 방식으로 접근한다.
    (0,0)에서 1칸씩 띄운 상태로 문자열을 배치하고, 모든 칸에 대해 두 문자열의
    문자를 비교하면서 서로 동일한 경우를 체크
    
3.  문자 비교에는 두 가지 경우가 존재
    1)  비교한 문자가 서로 같을 경우
        공통 수열에 포함되므로 바로 이전에 비교한 공통 수열 결과에 1을 더해
        그 값을 저장하는 것이고 바로 이전에 비교한 공통 수열의 결과는 두 문자열의
        1칸 씩 전에 위치하므로 table[i-1][j-1]의 값에 1을 더한 값이 된다.
    2)  비교한 문자가 서로 다를 경우
        바로 위 칸인 table[i-1][j]와 바로 왼쪽 칸인 table[i][j-1] 중 더 큰 값을 저장한다.
        두 칸은 해당 문자가 제거된 경우의 비교 결과이므로 두 값 중 더 큰 쪽이
        현재 위치에서의 가장 긴 공통 부분 수열이다.
"""

stringA = input().rstrip()
stringB = input().rstrip()

lenA = len(stringA)
lenB = len(stringB)

table = [[-1] * (lenB + 1) for _ in range(lenA + 1)]

for i in range(lenA + 1):
    for j in range(lenB + 1):
        if i == 0 or j == 0:
            table[i][j] = 0
        elif stringA[i - 1] != stringB[j - 1]:
            table[i][j] = max(table[i - 1][j], table[i][j - 1])
        elif stringA[i - 1] == stringB[j - 1]:
            table[i][j] = table[i - 1][j - 1] + 1

maxLength = -1

for i in range(lenA + 1):
    for j in range(lenB + 1):
        if maxLength < table[i][j]:
            maxLength = table[i][j]

print(maxLength)
