"""
10973번 이전 순열

1. 10972번 다음 순열 문제를 응용 / 수정하여 반대로 진행하는 문제.
    1) 뒤에서 부터 내림차순이 끊기는 지점을 선택
    2) 해당 지점의 수를 뒤쪽의 수 중 가장 가깝고 작은 수와 교환
    3) 해당 지점 뒤쪽을 내림차순으로 정렬
    4) 1)의 과정 중 끊기는 지점이 없다면 -1 출력
"""
import sys

N = int(input())

target = list(map(int, input().split()))

pivot = -1
diff = 0
idx = -1

for i in range(N - 1, -1, -1):
    if i == 0:
        print("-1")
        sys.exit()

    if target[i] < target[i - 1]:
        pivot = i - 1
        break

for i in range(pivot + 1, N):
    if target[pivot] > target[i] and target[i] > diff:
        diff = target[i]
        idx = i

temp = target[pivot]
target[pivot] = target[idx]
target[idx] = temp

target[pivot + 1 :] = sorted(target[pivot + 1 :], reverse=True)

for i in target:
    print(i, end=" ")
