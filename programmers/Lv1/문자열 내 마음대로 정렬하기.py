"""
    lv.1 문자열 내 마음대로 정렬하기
    
    1.  사전 순 정렬
    2.  인덱스 문자 순 정렬
"""


def solution(strings, n):
    answer = []

    strings.sort()
    strings.sort(key=lambda x: x[n])
    answer = strings

    return answer
