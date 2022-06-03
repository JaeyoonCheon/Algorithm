"""
2263번 트리의 순회

1.  inorder와 postorder로 표현된 트리를 preorder로 변환하는 문제.

2.  postorder에서 root를 구할 수 있고 그 root의 상대적 위치를 가지고
    inorder와 postorder의 수열을 일정 부분 잘라 좌/우 부분 트리에 대해
    재귀적으로 preorder순서대로 출력하면 됨.
"""

import sys

sys.setrecursionlimit(100001)

N = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

tree = {}


def makePreorder(inStart, inEnd, postStart, postEnd):
    if inStart > inEnd or postStart > postEnd:
        return

    root = postorder[postEnd]
    rootIdx = inorder.index(root)

    left = rootIdx - inStart
    right = inEnd - rootIdx

    print(root, end=" ")
    makePreorder(inStart, inStart + left - 1, postStart, postStart + left - 1)
    makePreorder(inEnd - right + 1, inEnd, postEnd - right, postEnd - 1)


makePreorder(0, N - 1, 0, N - 1)
