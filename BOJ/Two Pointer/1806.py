"""
1806번 부분 합

1.  주어진 수열에서 연속된 부분 수열이 S보다 클 경우의 최소 길이를 구하는 문제로,
    단순히 모든 부분 수열을 구하면 O(N^2) 시간복잡도가 걸릴 것으로 예상됨

2.  따라서, 수열의 처음부터 끝까지 나아가면서, 어떤 지점을 포인터로 가리킬 때
    shortest[N]은 해당 지점 N을 포함하고 끝으로 하는 합이 S이상이고 최소길이인 부분수열의
    길이를 저장하도록 지정하여 구현해봤다.

3.  처음에는 2)를 구현하기 쉽게 하기 위해 deque를 이용해 head/tail을 push/popleft로
    구현하고 그 deque의 합계를 sum함수로 구했는데 이렇게 할 경우 sum이 O(N)시간복잡도가 소요되고
    자료구조 또한 굳이 사용할 필요 없이 head/tail을 이용한 투포인터에
    포인터가 움직일 때 마다 합계에 합/차를 적용하는 것이 더 효율이라는 것을 알게 되었다.
"""

import sys, collections

N, S = map(int, input().split())

seq = list(map(int, sys.stdin.readline().split()))
length = len(seq)

head, tail = 0, 0

shortest = [0] * length

tempSeq = collections.deque()

currentSum = 0
currentLength = 0

while True:
    if head == length:
        break

    # tempSeq.append(seq[head])
    currentSum += seq[head]
    currentLength += 1

    while currentSum >= S:
        shortest[head] = currentLength
        currentSum -= seq[tail]
        currentLength -= 1
        tail += 1

    head += 1

minLength = 100001

for i in shortest:
    if i != 0 and i < minLength:
        minLength = i

if minLength == 100001:
    print(0)
else:
    print(minLength)
