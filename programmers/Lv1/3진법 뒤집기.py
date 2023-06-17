"""
    lv.1 3진법 뒤집기
    
    1.  n진법 -> 10진법 : 파이썬 int(숫자, n)
    2.  10진법 -> n진법 : n으로 숫자 나눠 몫+나머지로 진수
"""


def radix3(n):
    result = ""

    while n > 2:
        a, b = n // 3, n % 3
        n = a
        result = str(b) + result

    result = str(n) + result

    return result


def solution(n):
    answer = 0

    n3 = radix3(n)
    reversedN3 = n3[::-1]

    answer = int(reversedN3, 3)

    return answer


result = solution(45)
