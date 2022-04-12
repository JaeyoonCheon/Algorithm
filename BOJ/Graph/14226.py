"""
14226번 이모티콘

1.  BFS 이용한 최단 거리/횟수 문제

2.  고려해야할 최소 단위 :
    visited[emo][clipboard] = 화면에 emo개의 이모티콘이 있을 때,
    클립보드에 clipboard개의 이모티콘이 복사되어 있는 경우
    
3.  이 문제는 화면에 있는 이모티콘과 클립보드에 있는 이모티콘의 갯수의 변동에 따라
    경우의 수가 바뀔 수 있으므로, 2차원 배열을 사용하여 정보를 저장하고
    BFS를 실행해 최단 횟수를 탐색
"""

from collections import deque

S = int(input())

visited = [[False] * 1001 for _ in range(1001)]

q = deque()

visited[1][0] = True
q.appendleft((1, 1, 0))

while q:
    curr = q.pop()

    emo = curr[0]
    clipboard = curr[2]

    if emo == S:
        print(curr[1] - 1)
        break

    if emo > 0 and emo < 1001:
        if visited[emo][emo] == False:
            visited[emo][emo] = True
            q.appendleft((emo, curr[1] + 1, emo))

        attach = emo + clipboard
        if attach > 0 and attach < 1001:
            if visited[attach][clipboard] == False:
                visited[attach][clipboard] = True
                q.appendleft((attach, curr[1] + 1, clipboard))

        if visited[emo - 1][clipboard] == False:
            visited[emo - 1][clipboard] = True
            q.appendleft((emo - 1, curr[1] + 1, clipboard))
