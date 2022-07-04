"""
15666번 N과 M(12)

1.  백트래킹을 이용해 N개의 자연수 중에서 M개를 고른 수열을 만드는 문제.
    중복을 허용하며, 비 내림차순인 순열을 조건에 따라 만들면 풀 수 있다.
"""

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

newNumbers = list(sorted(set(numbers)))


def selectNumber(selected, prev):
    if len(selected) == M:
        for i in selected:
            print(i, end=" ")
        print()
        return

    for i in range(prev, len(newNumbers)):
        selected.append(newNumbers[i])
        selectNumber(selected, i)
        selected.pop()


selected = []

for i in range(len(newNumbers)):
    selected.append(newNumbers[i])
    selectNumber(selected, i)
    selected.pop()
