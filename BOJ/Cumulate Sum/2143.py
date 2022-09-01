"""
2143번 두 배열의 합

1.  일단 문제에서 '부 배열'이라는 단어에서 힌트를 얻어야 한다. 각 배열 A, B에서
    연속된(직접 언급은 x) 원소들로 이루어진 부분 배열으로 A의 부 배열과 B의 부 배열을
    합해 원하는 수 T가 나올 수 있도록 하는 문제이다.
    
2.  일단 '부 배열'을 구하기 위해 배열의 누적 합을 구해놓고, 인덱스의 처음부터 끝까지
    N^2 반복을 통해 누적 합의 차를 구함으로써 모든 부분 배열, 즉 모든 부 배열의 합을 구해
    저장해 놓을 수 있게 되었다.(자세한 원소는 어차피 합을 구할 것이므로 필요없다)

3.  이후, A에서 어떤 부 배열 X를 선택했을 때 B에 T-sum(X)인 합을 가진 부 배열이 존재하고 그 수를
    계산해 더해주면 해당 부 배열 쌍의 갯수를 셀 수 있다.
    따라서 구해놓은 부 배열합 리스트 partialAccB를 정렬한 뒤(이진 탐색을 위해!)
    partialAccA의 모든 원소에 대해 'T-원소'가 partialAccB의 어느 위치에 존재하는 지 이진 탐색으로
    lower_bound, upper_bound로 탐색해 그 존재와 갯수를 찾아 카운트해준다.
"""

import sys, bisect

T = int(input())

N = int(input())

A = list(map(int, sys.stdin.readline().split()))

M = int(input())

B = list(map(int, sys.stdin.readline().split()))

accA, accB = [], []

sumA = 0
sumB = 0

for i in A:
    sumA += i
    accA.append(sumA)

for j in B:
    sumB += j
    accB.append(sumB)

partialAccA, partialAccB = [], []

for i in range(len(accA)):
    for j in range(i, len(accA)):
        if j == i:
            partialAccA.append(accA[j])
        else:
            partialSum = accA[j] - accA[i]
            partialAccA.append(partialSum)

for i in range(len(accB)):
    for j in range(i, len(accB)):
        if j == i:
            partialAccB.append(accB[j])
        else:
            partialSum = accB[j] - accB[i]
            partialAccB.append(partialSum)


partialAccB.sort()

count = 0

for first in partialAccA:
    second = T - first

    startIdx = bisect.bisect_left(partialAccB, second)
    endIdx = bisect.bisect_right(partialAccB, second)

    count += endIdx - startIdx

print(count)
