"""
20040번 사이클 게임

1.  좁게 보면 그래프 간의 사이클을 발견하는 문제로 크루스칼 알고리즘이라고 볼 수 있다.
    하지만 크루스칼의 모든 아이디어를 사용할 필요는 없으며 개 중 union-find만 적용하여
    사이클을 검출하면 되는 문제이다.
    
2.  다만 파이썬 풀이 시 백준 저지에서 메모리 초과가 발생하는 것을 막기 위해 union-by-rank를 적용하여
    root 트리의 크기를 줄이는 것이 합리적이다.
"""

import sys

sys.setrecursionlimit(100000)

N, M = map(int, input().split())

root = [i for i in range(N)]


def find(v):
    if v == root[v]:
        return v
    root[v] = find(root[v])
    return root[v]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        if b > a:
            root[b] = a
        else:
            root[a] = b
        return True
    else:
        return False


isCycle = False

for i in range(M):
    _from, _to = map(int, sys.stdin.readline().split())

    if not isCycle:
        if not union(_from, _to):
            print(i + 1)
            isCycle = True
            break

if not isCycle:
    print(0)
