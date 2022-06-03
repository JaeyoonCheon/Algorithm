"""
1991번 트리 순회

1.  기본적인 트리의 전위/중위/후위 순회 방법.
"""

N = int(input())

tree = {}

for _ in range(N):
    root, left, right = input().split()

    tree[root] = (left, right)


def prefix(root):
    if root == ".":
        return
    print(root, end="")
    prefix(tree[root][0])
    prefix(tree[root][1])


def infix(root):
    if root == ".":
        return
    infix(tree[root][0])
    print(root, end="")
    infix(tree[root][1])


def postfix(root):
    if root == ".":
        return
    postfix(tree[root][0])
    postfix(tree[root][1])
    print(root, end="")


prefix("A")
print()

infix("A")
print()

postfix("A")
