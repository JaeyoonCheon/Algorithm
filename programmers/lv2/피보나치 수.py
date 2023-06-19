"""
    lv.2 피보나치 수
    
    1.  반복문으로 구현
"""


def solution(n):
    answer = 0

    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    answer = a % 1234567

    return answer
