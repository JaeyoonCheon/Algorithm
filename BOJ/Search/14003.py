"""
14003번 가장 긴 증가하는 부분 수열 5

1.  LIS(가장 긴 증가하는 부분 수열) 문제이다.
    다른 LIS문제와의 차이점은 주어지는 입력의 길이가 백만단위라는 것이므로
    DP를 이용한 O(N^2) 방법으로는 시간이 너무 오래 걸린다.
    
2.  따라서, DP에서 각 인덱스가 의미하는 "현재 위치의 수가 마지막이 되도록 하는 LIS"와 유사하지만 다르게
    LIS를 유지해가면서 수열의 각 숫자들을 현재 LIS에 비교해 대체되거나 추가시켜나가는 방법을 사용한다.
    이 때, 유지된 LIS(정렬된 상태이다)에 자신보다 같거나 큰 수의 위치를 찾아 대체하거나 마지막에 추가하는 것이므로
    전자의 인덱스를 찾기 위해 O(logN)인 이진 탐색법을 적용하면 총 시간복잡도가 O(NlogN)에 해결할 수 있다.

3.  2)의 계산 중 각 수가 LIS의 몇 번째 인덱스에 위치해야 LIS를 유지할 수 있는지를 record에 저장한 후,
    record에 저장된 수를 뒤에서부터 가장 큰 수 ~ 가장 작은 수까지 1씩 차이나는 수를 찾아 역순으로 배열하면
    곧 LIS 중 하나의 case가 나타난다.
"""

import sys, bisect

N = int(input())

seq = list(map(int, sys.stdin.readline().split()))
record = []

lis = []
lis.append(seq[0])
record.append(0)

for i in range(1, N):
    if lis[-1] >= seq[i]:
        idx = bisect.bisect_left(lis, seq[i])
        lis[idx] = seq[i]
        record.append(idx)
    else:
        lis.append(seq[i])
        record.append(len(lis) - 1)

print(len(lis))

start = max(record)
lis = []

for i in range(len(seq) - 1, -1, -1):
    if record[i] == start:
        lis.append(seq[i])
        start -= 1

lis.reverse()

for i in lis:
    print(i, end=" ")
