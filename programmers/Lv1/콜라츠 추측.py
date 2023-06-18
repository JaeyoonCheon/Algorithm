"""
    lv.2 콜라츠 추측
    
    1.  단순 반복 문제. 반복문이나 재귀 어느것으로 구현해도 무방
"""


def operation(num, cnt):
    if cnt == 500:
        return -1
    if num == 1:
        return cnt

    if num % 2 == 0:
        return operation(num // 2, cnt + 1)
    else:
        return operation(num * 3 + 1, cnt + 1)


def solution(num):
    answer = operation(num, 0)

    return answer
