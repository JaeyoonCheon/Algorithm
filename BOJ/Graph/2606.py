"""
2606번 바이러스

1.  인접한 컴퓨터들의 연결에서 1번 컴퓨터가 감염되었을 때 영향받는 컴퓨터들의 수.
    따라서, 1번 컴퓨터는 개수에서 제외된다.
    
2.  1번 노드에 연결된 노드들의 수를 찾는 그래프 문제로, dfs를 응용하여 해결
"""

N = int(input())

couple = int(input())

computers = [[] for _ in range(N + 1)]

for _ in range(couple):
    start, end = map(int, input().split())
    computers[start].append(end)
    computers[end].append(start)

visited = [False] * (N + 1)

count = 0


def dfs(point):
    global count
    visited[point] = True
    count += 1

    for next in computers[point]:
        if not visited[next]:
            dfs(next)

    return


dfs(1)

print(count - 1)
