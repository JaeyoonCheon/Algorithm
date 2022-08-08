"""
9252번 LCS 2

1.  LCS(Longest Common Subsequence), 최장 공통 부분수열을 구하는 문제이다.

2.  LCS의 길이는 두 문자열을 축으로 하는 이차원 배열에서 dp를 이용해 푸는 것이 간편하다.

3.  LCS 값 자체를 구하는 것은 LCS의 길이인 배열 가장 마지막 값에서 출발해
    역순으로 왼쪽/위쪽의 값이 동일한 위치로 돌아가다가 모두 값이 현재 값과 다를 경우
    이전 저장된 LCS길이의 위치로 이동하는데, 이 때의 현재 값을 저장해 놓고
    0을 만날 때 까지 반복한다.
    이후, 저장된 값을 반전하면 LCS를 구할 수 있다.
    (LCS는 여러 개의 케이스가 있을 수 있다.)
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

if maxLength != 0:
    result = []
    curr = table[lenA][lenB]
    currX, currY = lenA, lenB

    while curr != 0:
        if curr == table[currX - 1][currY]:
            curr = table[currX - 1][currY]
            currX -= 1
            continue
        elif curr == table[currX][currY - 1]:
            curr = table[currX][currY - 1]
            currY -= 1
            continue

        curr = table[currX - 1][currY - 1]
        currX -= 1
        currY -= 1
        result.append(stringA[currX])

    result.reverse()

    lcs = "".join(result)
    print(lcs)
