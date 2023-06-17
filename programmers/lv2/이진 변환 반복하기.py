"""
    lv.2 이진 변환 반복하기
    
    1.  문자열에서 0의 개수를 카운트하고 ""로 대체
    2.  대체된 문자열의 길이를 2진 변환한 결과 반환
    3.  1~2의 과정을 1이 될 때 까지 반복
"""


def radix2(n):
    result = ""

    while n > 1:
        a, b = n // 2, n % 2
        n = a
        result = str(b) + result

    result = str(n) + result

    return result


def solution(x):
    totalZero = 0
    iter = 0

    while x != "1":
        iter += 1
        zeroCnt = x.count("0")
        totalZero += zeroCnt
        x = x.replace("0", "")
        x = str(radix2(len(x)))

    return [iter, totalZero]


result = solution("01110")
print(result)
