"""
1260번 DFS와 BFS

1. DFS/BFS 구현
"""

N, M, V = map(int, input().split())

edge = [[] for _ in range(N + 1)]
q = []

for i in range(M):
    _from, _to = map(int, input().split())
    edge[_from].append(_to)
    edge[_to].append(_from)

for i in edge:
    i.sort()


def dfs(vertex, depth):
    visited[vertex] = True
    print(vertex, end=" ")

    if depth == N:
        return

    for i in edge[vertex]:
        if visited[i] == True:
            continue
        dfs(i, depth + 1)


def bfs(start):
    visited[start] = True
    q.insert(0, start)

    while q:
        vertex = q.pop()
        print(vertex, end=" ")

        for i in edge[vertex]:
            if visited[i] == False:
                visited[i] = True
                q.insert(0, i)


visited = [0] * (N + 1)
visited[0] = True

dfs(V, 0)

print()

visited = [0] * (N + 1)
visited[0] = True

bfs(V)
