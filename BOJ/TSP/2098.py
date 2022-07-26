"""
2098번 외판원 순회

1.  Traveling Salesman Problem(TSP) 문제로 1~N번의 도시를 한번씩만 경유한 뒤
    출발한 원래 도시로 돌아오는 경로 중 가장 작은 길이의 경로를 찾는 문제.
    NP-hard문제이고 동적계획법을 사용하지 않으면 O(N!), 사용하면 O(N^2*2^N)인 문제.

2.  기본적인 완전 탐색으로는 모든 도시 city에 대해서 city로 돌아오는 경로를 모두 탐색해보는데,
    어떤 도시에서 아직 탐색하지 않았고 갈 수 있는 도시에 대해 재귀적으로 탐색하는 방법이다.

3.  완전탐색을 개선하기 위해 DP를 적용해보도록 한다.
    1)  경로 자체를 요구하지 않기 때문에 비트마스킹을 사용해 방문 여부만 확인하면 된다.
    2)  findPath() 함수는 분명히 재귀호출 도중에 중복되어 DP로 개선 가능
    3)  어떤 최소 경로 P는 어느 도시에서 출발해도 거리 자체는 동일하다. 즉 출발 도시를 고정해도 무방
    4)  메모이제이션 대상은 어떤 도시에서 다른 도시로 이동하는 경로의 최소 거리이다.
"""

N = int(input())

G = [list(map(int, input().split())) for _ in range(N)]


def TSP_Bruteforce():
    minDist = float("inf")
    VISIT_N = (1 << N) - 1

    def findPath(start, currEnd, visited, currDist):
        nonlocal minDist

        if visited == VISIT_N:
            last_path = G[currEnd][start] or float("inf")
            minDist = min(minDist, currDist + last_path)
            return

        for city in range(N):
            if visited & (1 << city) == 0 and G[currEnd][city] != 0:
                findPath(start, city, visited | (1 << city), currDist + G[currEnd][city])

    for i in range(N):
        findPath(i, i, 1 << i, 0)

    return minDist


def TSP_DP():
    VISIT_N = (1 << N) - 1
    dp = [[None] * (1 << N) for _ in range(N)]

    def findPath(last, visited):
        if visited == VISIT_N:
            return G[last][0] or float("inf")

        if dp[last][visited] is not None:
            return dp[last][visited]

        result = float("inf")
        for city in range(N):
            if visited & (1 << city) == 0 and G[last][city] != 0:
                result = min(result, findPath(city, visited | (1 << city)) + G[last][city])

        dp[last][visited] = result
        return result

    return findPath(0, 1 << 0)


print(TSP_DP())
