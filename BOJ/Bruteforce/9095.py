"""
9095번 1,2,3 더하기

1. DP
N = 4
1 + 3
2 + 2
3 + 1

N = 5
2 + 3
3 + 2
4 + 1

위와 같이 n을 만드는 경우의 수는 n에서 1을 뺀 값 + 2를 뺀 값 + 3을 뺀 값을 더한 경우이다.
따라서, A(N)=A(N-1)+A(N-2)+A(N-3)이다.

2. 재귀
주어진 N에서 1, 2, 3을 순차적으로 재귀함수에 전달, 더하여 만들 수 있는 경우의 수를 탐색
재귀를 쉽게 구현하기 위하여 더하지 않고 역으로 N에서 1, 2, 3을 차감하여 재귀식을 구성하였고
종료 조건은 0이 되면 카운트 1을 반환, 0보다 작아지면 카운트를 증가시키지 않으므로 0을 반환
"""


def calculateDP(N):
    # 초기값
    data = [0, 1, 2, 4]

    for i in range(4, N + 1):
        data.append(data[i - 1] + data[i - 2] + data[i - 3])

    return data[N]


def calculateRecursive(N):
    if N == 0:
        return 1
    elif N < 0:
        return 0
    else:
        return (
            calculateRecursive(N - 1)
            + calculateRecursive(N - 2)
            + calculateRecursive(N - 3)
        )


iter = int(input())

for _ in range(iter):
    N = int(input())
    print(calculateDP(N))
    print(calculateRecursive(N))
