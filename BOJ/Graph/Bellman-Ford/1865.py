"""
1865번 웜홀

1.  이 문제에서 요구하는 것은 인접리스트로 주어진 그래프에 대해 한 지점에서 출발하여 다시 돌아왔을 때
    시간이 되돌아간, 즉 걸린 시간이 음수인 경로가 있는 지 조사하는 문제이다.
    주어진 그래프는 가중치가 음수를 포함하며, 도로는 양방향이고 가중치가 음인 웜홀은 단방향이다.
    
2.  고로 그래프에 음수 사이클이 존재 하는지 검사하는 문제로, 음수 가중치를 다룰 수 있는 대표적인 방법이
    플로이드-와샬과 벨만-포드 알고리즘이 있다. 다만 플로이드 알고리즘은 모든 정점에서의 거리를 검사하므로, 
    시간 효율적인 측면에서 좋지 않을 것으로 판단되어 벨만-포드 알고리즘을 적용해 문제를 해결했다.
    
3.  벨만 포드 알고리즘은
    1)  한번이라도 방문한 정점에 대해 최단거리를 갱신
    2)  1)의 과정을 정점 개수 - 1만큼 반복
    3)  음수 사이클을 찾기 위해 한번 더 검사하고 최단거리가 갱신되는 지점이 있다면
        음수 사이클이 존재한다는 의미
    의 과정을 통해 풀이된다.
    
4.  하지만, 이 문제에서 어떤 임의의 정점을 선택해 출발했을 때 음수 사이클에 도달할 수 없는 경우가
    생길 수 있다. 따라서 이 부분을 해결하기 위한 방법으로 2가지 방식이 생각될 수 있다.
    1)  한번이라도 방문한 정점에 대해서만 최단거리를 갱신하는 경우
        1-1)    모든 최단거리를 0으로 초기화시켜 모든 정점에서 동시에 시작하도록 조정
        1-2)    어떤 가짜 정점 N+1을 만들고 모든 정점에 가중치 0으로 연결되도록 한 후
                N+1에서 시작하면 모든 정점에 도달할 수 있으므로 음수 사이클에 무조건 도달 가능
    2)  모든 정점에 대해 최단거리를 갱신하는 경우
        이 경우는 위의 1-1)과 유사하게 한 곳에서 시작했어도 모든 정점이 갱신됨  
"""

INF = 5000 * 10000

T = int(input())


def BF_AllNode(N, G):
    dist = [INF] * (N + 1)

    """시작지점 1번에서 출발"""
    dist[1] = 0

    for _ in range(1, N + 1):
        for i in range(1, N + 1):
            for j in G[i]:
                if dist[j[0]] > dist[i] + j[1]:
                    dist[j[0]] = dist[i] + j[1]

    isMinusCycle = False

    for i in range(1, N + 1):
        for j in G[i]:
            if dist[i] == INF:
                continue
            else:
                if dist[j[0]] > dist[i] + j[1]:
                    isMinusCycle = True

    if isMinusCycle:
        print("YES")
    else:
        print("NO")


def BF_ZeroNode(N, G):
    dist = [0] * (N + 1)

    """시작지점 1번에서 출발"""
    dist[1] = 0

    for _ in range(1, N + 1):
        for i in range(1, N + 1):
            for j in G[i]:
                if dist[i] == INF:
                    continue
                else:
                    if dist[j[0]] > dist[i] + j[1]:
                        dist[j[0]] = dist[i] + j[1]

    isMinusCycle = False

    for i in range(1, N + 1):
        for j in G[i]:
            if dist[i] == INF:
                continue
            else:
                if dist[j[0]] > dist[i] + j[1]:
                    isMinusCycle = True

    if isMinusCycle:
        print("YES")
    else:
        print("NO")


def BF_AnotherNode(N, G):
    dist = [0] * (N + 1)

    temp = [(i, 0) for i in range(1, N + 1)]
    G.insert(N + 1, temp)

    """시작지점 N+1번(가짜 노드)에서 출발"""
    dist.append(0)

    for _ in range(1, N + 2):
        for i in range(1, N + 2):
            for j in G[i]:
                if dist[i] == INF:
                    continue
                else:
                    if dist[j[0]] > dist[i] + j[1]:
                        dist[j[0]] = dist[i] + j[1]

    isMinusCycle = False

    for i in range(1, N + 2):
        for j in G[i]:
            if dist[i] == INF:
                continue
            else:
                if dist[j[0]] > dist[i] + j[1]:
                    isMinusCycle = True

    if isMinusCycle:
        print("YES")
    else:
        print("NO")


for _ in range(T):
    N, M, W = map(int, input().split())

    G = [[] for _ in range(N + 1)]

    for _ in range(M):
        S, E, T = map(int, input().split())

        G[S].append((E, T))
        G[E].append((S, T))

    for _ in range(W):
        S, E, T = map(int, input().split())

        G[S].append((E, -1 * T))

    BF_AnotherNode(N, G)
