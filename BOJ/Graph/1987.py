"""
1987번 알파벳

1.  전형적인 백트래킹 문제로 보인다.
    dfs로 (0,0)에서 뻗어나가 상하좌우 4방향 보드칸의 A~Z까지의 방문 여부를 체크하고 최대 경로 길이를 저장한다.
    
2.  알파벳은 문자로 입력되므로, 소문자로 바꾼 뒤 a의 아스키코드값 97을 제하여 인덱스를 만들어 주었다.
    소문자 변환 과정도 불필요할 듯 하며 26길이의 list를 쓰는 것이 아닌 비트마스킹을 이용하면
    휠씬 더 빠르게 확인과정을 거칠 수 있을 것으로 생각된다.
"""

R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

maxLength = 0

visiting = [False] * 26


def checkBorder(x, y):
    if x < 0 or x >= R or y < 0 or y >= C:
        return False
    return True


def findPath(x, y, count):
    global maxLength

    if count > maxLength:
        maxLength = count

    for i in range(4):
        if checkBorder(x + dx[i], y + dy[i]):
            next = board[x + dx[i]][y + dy[i]].lower()
            if not visiting[ord(next) - 97]:
                visiting[ord(next) - 97] = True
                findPath(x + dx[i], y + dy[i], count + 1)
                visiting[ord(next) - 97] = False


visiting[ord(board[0][0].lower()) - 97] = True
findPath(0, 0, 1)

print(maxLength)
