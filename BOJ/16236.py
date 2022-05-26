"""
16236번 아기 상어
"""

import collections

N = int(input())

space = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

currentSize = 2
eatenFish = 0

def findCandidate(x, y, dist):
    visited = [[False]*N for _ in range(N)]
    q = collections.deque()
    
    q.append((x, y))
    visited[x][y] = True
    
    while q:
        curr = q.popleft()
        canMove = []
        
        for dir in range(4):
            if space[curr[0]+dx[dir]][curr[1]+dy[dir]] > currentSize:
                continue
            else:
                