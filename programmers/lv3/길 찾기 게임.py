"""
    lv.3 길 찾기 게임
    
    1.  이진 트리를 주어진 문제의 예시대로 구현하여 preorder/postorder를 시행
    2.  노드의 정보로 주어진 리스트에 인덱스 번호를 추가하고, y좌표로 정렬하여 트리에 삽입해야 한다.
"""

import sys

sys.setrecursionlimit(10**6)


class Btree:
    def __init__(self, info):
        self.number = info[0]
        self.x = info[1]
        self.y = info[2]
        self.left = None
        self.right = None

    def addNode(self, info):
        if self.x < info[1]:
            if self.right:
                self.right.addNode(info)
            else:
                self.right = Btree(info)
        else:
            if self.left:
                self.left.addNode(info)
            else:
                self.left = Btree(info)

    def preorder(self, order):
        order.append(self.number)
        if self.left:
            order = self.left.preorder(order)
        if self.right:
            order = self.right.preorder(order)

        return order

    def postorder(self, order):
        if self.left:
            order = self.left.postorder(order)
        if self.right:
            order = self.right.postorder(order)
        order.append(self.number)

        return order


def solution(nodeinfo):
    answer = []

    nodeinfo = [[i + 1, v[0], v[1]] for i, v in enumerate(nodeinfo)]
    nodeinfo = sorted(nodeinfo, key=lambda x: x[2], reverse=True)

    binTree = Btree(nodeinfo[0])

    for info in nodeinfo[1:]:
        binTree.addNode(info)

    answer.append(binTree.preorder([]))
    answer.append(binTree.postorder([]))

    return answer


result = solution(
    [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
)
