"""
    lv.2 전화번호 목록
    
    1.  전화번호부의 전화번호들을 딕서너리에 우선 등록.
    2.  전화번호 하나하나들을 앞에서부터 분해해 만들 수 있는 접두사 조합들에 대해,
        전화번호와 동일하지 않은 접두사가 존재할 경우 참.
    3.  전화번호부를 정렬하면 아스키코드 순으로 정렬되므로, 어떤 번호가 바로 앞의 번호를 접두사로 가질 확률이 높다.
        따라서, 이전 번호+다음 번호를 zip으로 묶어 서로 간 접두사인지 확인하는 풀이를 생각할 수 있다.
"""


def sortAndZip(phone_book):
    phone_book.sort()

    for first, second in zip(phone_book, phone_book[1:]):
        if second.startsWith(first):
            return False

    return True


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
