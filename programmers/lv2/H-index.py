"""
    lv.2 H-index
    
    1.  논문 n편 중 h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었을 때,
        h가 될 수 있는 값의 최대값
    2.  정렬한 뒤 뒤에 위치하는 논문들의 길이를 현재 논문의 인용 횟수와 비교하는 것이 가장 간단.
"""


def solution(citations):
    citations.sort()

    for i, c in enumerate(citations):
        if c >= len(citations) - i:
            return len(citations) - i

    return 0
