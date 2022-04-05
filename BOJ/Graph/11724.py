"""
11724번 연결 요소의 갯수

1.  dfs이용, 각 방문하지 않은 정점을 발견할 때 마다 dfs를 시행해
    연결된 요소들을 모두 방문 처리하고, 연결 요소의 갯수를 +1하면 풀 수 있다.
    
2.  다만, python3 컴파일러에서는 입력값과 재귀 깊이에 제한이 있어
    setRecursionLimit을 설정해주고 sys.stdin.readline()을 사용해야 통과할 수 있을 것
    pypy3은 재귀 깊이에 여유가 있어 통과 가능하다.
"""

import sys

N, M = map(int, input().split())

edge = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
    _from, _to = map(int, sys.stdin.readline().split())
    edge[_from].append(_to)
    edge[_to].append(_from)


def dfs(v, depth):
    visited[v] = True

    if depth == N:
        return

    for i in edge[v]:
        if visited[i] == True:
            continue
        dfs(i, depth + 1)


count = 0

for i in range(1, N + 1):
    if visited[i] == False:
        count += 1
        dfs(i, 0)

print(count)
