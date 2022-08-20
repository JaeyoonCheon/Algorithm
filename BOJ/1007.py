"""
1007번 벡터 매칭

1.  주어진 (x, y)의 좌표들의 집합에서 두 점끼리의 벡터의 합의 길이가 최소가 되는 값을 구하는 문제.
    이 때 모든 좌표들은 한 번 씩만 방문되어야 한다.
    
2.  처음 풀이에서는 정직하게 모든 좌표에 대해 2개를 뽑아 나열하는 순열을 통해 모든 가능한 벡터 조합을 구하고
    그 벡터들에서 N//2개를 골라 만든 벡터합의 최소 길이를 완전탐색으로 구했다. 그 결과 최대 (20P2)C10을 구해야하므로 경우의 수와 필요한 공간이
    너무나 많아진다.
    
3.  관점을 바꿔, A->B의 벡터는 원점에서의 벡터 O->B에서 O->A를 뺀 것과 같다. 그리고 벡터 연산 시 각각의 x, y좌표를 따로 저장하는 것이 효율적일 것이다.
    따라서, 구한 벡터들에서 x, y 각각의 좌표값을 모두 더한 벡터 총 합을 저장해놓고 N//2개의 벡터를 뽑아 총합에서 2번 제한다면
    값을 구할 수 있다.
"""

import itertools, copy
from math import sqrt

T = int(input())

for _ in range(T):
    N = int(input())

    vectors = [list(map(int, input().split())) for _ in range(N)]

    total = [0, 0]

    for i in vectors:
        total[0] += i[0]
        total[1] += i[1]

    vectorsComb = list(itertools.combinations(vectors, N // 2))

    def vectorSize(vectorMatch):
        totalSum = copy.deepcopy(total)
        matchingSum = [0, 0]

        for i in vectorMatch:
            matchingSum[0] += i[0]
            matchingSum[1] += i[1]

        result = [totalSum[0] - matchingSum[0] * 2, totalSum[1] - matchingSum[1] * 2]

        return sqrt(result[0] ** 2 + result[1] ** 2)

    vectorMatchings = list(map(vectorSize, vectorsComb))

    print(min(vectorMatchings))
