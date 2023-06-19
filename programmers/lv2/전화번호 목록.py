"""
    lv.2 전화번호 목록
    
    1.  전화번호부의 전화번호들을 딕서너리에 우선 등록.
    2.  전화번호 하나하나들을 앞에서부터 분해해 만들 수 있는 접두사 조합들에 대해,
        전화번호와 동일하지 않은 접두사가 존재할 경우 참.
"""


def solution(phone_book):
    phoneDict = {}

    for pn in phone_book:
        phoneDict[pn] = True

    for pn in phone_book:
        partial = ""

        for c in pn:
            partial += c

            if partial in phoneDict and partial != pn:
                return False

    return True
