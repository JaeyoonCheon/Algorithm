"""
5430번 AC

1.  처음 문제를 봤을 때 리스트에 저장 후 reverse()와 pop(0)로 풀이할 수 있겠다고
    생각했으나 구현 뒤 체크해 보니 시간 초과를 받았다.
    reverse()와 pop(0) 모두 리스트 모든 개체를 순회해야하기 때문에 O(N) 시간복잡도가
    걸리므로 1초 내에 해결하는 조건에는 부합하지 않았다.

2.  pop(0) 연산이 O(N)이 걸리므로 slicing을 이용했으나 여전히 시간초과.

3.  우선, 자료구조를 더 효율적인 deque로 전화하고, reverse 연산을 최소로 하기 위해
    연달아 주어지는 reverse 연산은 명령에서 삭제했다.

4.  그러함에도 명령의 최대 길이가 100000이므로, reverse() 연산이 삭제되지 않을 경우에는
    시간 초과가 발생할 것이므로, deque의 특성을 이용해 reverse 연산일 때 방향을 전환하고
    해당 방향에서 deque의 pop / popleft 연산을 수행하고 마지막에 reverse()가
    홀수 번 나왔는 지 짝수 번 나왔는지를 계산해 뒤집어줄 지 결정.

5.  시간 관리를 위해 생각해 주어야 할 테크닉이 많은 문제.
"""

import collections

T = int(input())

for _ in range(T):
    func = list(input().replace("RR", ""))
    N = int(input())

    if N:
        arr = collections.deque(map(int, input()[1:-1].split(",")))
    else:
        input()
        arr = []

    isError = False
    isReverse = func.count("R")
    dir = 1

    for op in func:
        if op == "R":
            dir *= -1
        else:
            if arr:
                if dir == 1:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                isError = True
                break

    if isError:
        print("error")
    else:
        if isReverse % 2 == 1:
            arr.reverse()

        print("[", end="")
        for i in range(len(arr)):
            if i == len(arr) - 1:
                print(f"{arr[i]}", end="")
                break
            print(f"{arr[i]},", end="")
        print("]")
