"""
1005번 ACM Craft

1.  순서를 뒤집어 생각해 봐야할 문제.
    건물이 완성되기 위해서는 선행 건물들이 모두 완료되어 있어야 건설이 가능하다.
    선행 건물 중 시작 시점으로부터 건설이 가장 오래걸리는 건물이 완료되면 그 즉시 건설 가능하다고 간주하므로
    선행 건물들 중의 총 건설 기간 중 가장 큰 값을 가져와 자신의 건설 시간을 덧붙이면 결과를 구할 수 있다.
    
2.  예외 케이스로, 모든 건물들의 건설 시간이 0일 경우에 메모이제이션 배열의 초기화를 False로 해놓으면
    0이 False로 간주되므로 무한히 재귀되는 현상이 생길 수 있어 초기화는 -1로 해주어야 한다.
"""

import sys

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())

    D = list(map(int, sys.stdin.readline().split()))
    D.insert(0, 0)

    G = [[] for _ in range(N + 1)]

    for _ in range(K):
        _from, _to = map(int, sys.stdin.readline().split())

        G[_to].append(_from)

    W = int(input())

    visited = [-1] * (N + 1)

    def construction(node):
        wayPoint = []

        if G[node]:
            for i in G[node]:
                if visited[i] == -1:
                    wayPoint.append(construction(i) + D[node])
                else:
                    wayPoint.append(visited[i] + D[node])

            visited[node] = max(wayPoint)
            return visited[node]
        else:
            visited[node] = D[node]
            return D[node]

    print(construction(W))
