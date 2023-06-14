"""
    lv.1 달리기 경주
    
    1. 단순 배열 인덱스 탐색 -> 스왑의 경우 배열에서 인덱스를 탐색하는 데 너무 과도한 시간이 소요.
    2. 따라서, 선수마다 이름에 대한 순위를 mapping 해 놓고 인덱스를 O(1)시간에 찾는 방식으로 해결
"""


def simpleSwap(players, callings):
    answer = []

    for call in callings:
        idx = players.index(call)

        players[idx - 1], players[idx] = players[idx], players[idx - 1]

    answer = players
    return answer


def mapIndex(players, callings):
    dict = {}

    for i, v in enumerate(players):
        dict[v] = i

    for call in callings:
        idx = dict[call]
        beforePlayer = players[idx - 1]

        players[idx - 1], players[idx] = players[idx], players[idx - 1]
        dict[call], dict[beforePlayer] = dict[beforePlayer], dict[call]

    return players


def solution(players, callings):
    return mapIndex(players, callings)


solution()
