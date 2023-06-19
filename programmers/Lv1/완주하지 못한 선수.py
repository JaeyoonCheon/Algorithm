"""
    lv.1 완주하지 못한 선수
    
    1.  참여자 딕셔너리 생성(값으로는 나타난 횟수를 나타날 때 마다 1씩 증가시키며 저장)
    2.  완주자 목록에 대해, 참여자 딕셔너리의 값을 1씩 뺀다.
    3.  한 명이 완주를 못해 1이 값에 존재하는 키를 반환
"""


def solution(participant, completion):
    answer = {}

    for p in participant:
        answer[p] = answer.get(p, 0) + 1

    for c in completion:
        answer[c] -= 1

    for x in answer:
        if answer[x]:
            return x
