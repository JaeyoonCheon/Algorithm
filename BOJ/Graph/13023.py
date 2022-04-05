"""
10323번 ABCDE

1.  A는 B와 친구다.
    B는 C와 친구다.
    C는 D와 친구다.
    D는 E와 친구다.
    
    이 조건의 뜻은 연속되는 친구 관계가 4쌍이 존재하면 문제 조건에 성립하는 것이다.
    
2.  따라서, 2차원 배열에 친구 관계를 쌍으로 집어넣고 dfs를 실행해
    depth가 4이상 진행되는 경우를 판정
"""

N, M = map(int, input().split())

friends = [[] for _ in range(N)]
visited = []

for i in range(M):
    _from, _to = map(int, input().split())
    friends[_from].append(_to)
    friends[_to].append(_from)

flag = 0


def check(num, depth):
    global flag
    visited[num] = 1

    if depth == 4:
        flag = 1
        print(1)
        exit()

    if 0 not in visited:
        return

    for i in friends[num]:
        if visited[i] == 1:
            continue
        check(i, depth + 1)

    visited[num] = 0


for i in range(N):
    visited = [0] * N
    check(i, 0)

print(flag)
