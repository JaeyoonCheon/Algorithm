"""
5639번 이진 검색 트리

1.  이 문제는 주어진 전위순회(prefix)로 표현된 이진 트리의 값을 후위 순회(postfix)로 변환해 출력해야 하는 문제이다.

2.  기본적으로 생각해 볼 수 있는 방식으로는, 전위순회 입력을 받아 root-left-right 순서로 쪼개 다시 트리를 구성하고
    만들어진 트리를 후위순회로 읽어 반환하는 방법을 선택할 수 있겠다.
    
3.  하지만, 객체로 다시 트리를 구성하는 것 자체가 시간 효율에 있어 좋지 않다고 판단하였고
    따라서 전위순회로 주어진 수열을 후위순회식으로 찾아 재귀적으로 root를 출력하는 방식을 선택했다.
    
4.  범위를 투포인터로 받아와 그 첫번째 인덱스는 무조건 서브트리의 root이다.
    해당 root 다음 수부터 자식 노드인데, root보다 큰 지점부터 오른쪽 자식 트리이고
    root 다음부터 그 지점 전까지가 왼쪽 자식 트리이다.
    
5.  위 방법으로 트리를 재귀적으로 순회 가능하고 후위 순회 방식인 left-right-root 순서대로
    방문해 출력하면 해결할 수 있다.
"""

import sys

sys.setrecursionlimit(100000)

inputData = sys.stdin.readlines()

prefix = []

for data in inputData:
    prefix.append(int(data))


def toPostfix(start, end):
    if end - start == 0:
        return

    root = prefix[start]
    rightStart = end

    for i in range(start, end):
        if prefix[i] > root:
            rightStart = i
            break

    if end - start > 1:
        toPostfix(start + 1, rightStart)
        toPostfix(rightStart, end)
    print(root)


toPostfix(0, len(prefix))
