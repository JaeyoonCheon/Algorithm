"""
10972번 다음순열

1. 백트래킹
    순열을 백트래킹으로 처음부터 만들어가면서 목표하는 순열을 찾을 경우, 다음 순열을 출력하도록 구성
    
    문제) 이 문제에서 N = 10000까지 증가할 수 있으므로 재귀 깊이 또한 10000까지 증가한다.
    이러한 경우 시간 제한 1초 안에 문제를 해결할 수 없고 파이썬 재귀 제한에도 걸려 별도 모듈을 import해야 하는 문제가 있다.
    
2. '다음 순열'에 대한 규칙성
    한 오름차순 순열이 다음 순열이 되기 위한 규칙성을 생각
    
    1) 순열의 뒤쪽에서부터 고려하여 오름차순이 멈추는 다음 지점을 찾는다.
    ex) 2 1 4 3 -> 1 지점
    
    2) 그 수와 뒤쪽에 위치한 수들 사이에서 가장 가깝게 큰 수와 교환한다.(가깝다는 것은 크기 척도 면에서 가까운 것을 의미)

    3) 이후 그 지점 뒤쪽의 수들을 오름차순으로 정렬한다.

    4) 지점의 index가 -1이라면 더 이상 증가할 수 있는 순열이 존재하지 않는다.
"""

from cmath import pi
import sys

"""
시간 초과
import sys

sys.setrecursionlimit(100000)

flag = False


def makeSeq(N, seq, target):
    global flag
    if len(seq) == N:
        if flag == True:
            for j in range(len(seq)):
                print(seq[j], end=" ")
            flag = False

        if seq == target:
            flag = True
        return

    for i in range(1, N + 1):
        if i in seq:
            continue
        seq.append(i)
        makeSeq(N, seq, target)
        seq.pop()


N = int(input())

target = list(map(int, input().split()))
seq = []

makeSeq(N, seq, target)

if flag == True:
    print("-1")
    """

N = int(input())

target = list(map(int, input().split()))

pivot = -1
diff = 10001
idx = -1

for i in range(N - 1, -1, -1):
    if i == 0:
        print("-1")
        sys.exit()

    if target[i] > target[i - 1]:
        pivot = i - 1
        break

for i in range(pivot + 1, N):
    if target[pivot] < target[i] and target[i] < diff:
        diff = target[i]
        idx = i

temp = target[pivot]
target[pivot] = target[idx]
target[idx] = temp

target[pivot + 1 :] = sorted(target[pivot + 1 :])

for i in target:
    print(i, end=" ")
