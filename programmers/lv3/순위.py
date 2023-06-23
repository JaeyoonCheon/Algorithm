"""
    lv.3 순위
"""

from collections import defaultdict


def solution(n, results):
    answer = 0

    win = defaultdict(set)
    lose = defaultdict(set)

    for winner, loser in results:
        # winner는 loser를 이겼음
        win[winner].add(loser)
        # loser는 winner에게 졌음
        lose[loser].add(winner)

    # n번 선수는
    for i in range(1, n + 1):
        # loser들을 이겼으니 loser들은 n번 선수가 진 사람들에게 무조건 진다.
        for loser in win[i]:
            lose[loser].update(lose[i])
        # winner들에게 졌으니 winner들은 n번 선수가 이긴 사람들에게 무조건 이긴다.
        for winner in lose[i]:
            win[winner].update(win[i])

    # 승 + 패 의 횟수가 n - 1인 경우 정확한 순위를 가릴 수 있는 경우.
    for i in range(1, n + 1):
        loseCnt, winCnt = len(lose[i]), len(win[i])

        if loseCnt + winCnt == n - 1:
            answer += 1

    return answer


result = solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
