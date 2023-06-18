"""
    lv.2 소수 찾기
    
    1.  numbers에서 만들 수 있는 모든 조합의 수에 대해 소수 판별
    2.  permutations에서 생성된 튜플 조합에 대해 중복 제거 & 평탄화 작업 후 소수 판병
"""


def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


import itertools


def solution(numbers):
    answer = 0

    cases = []
    for r in range(1, len(numbers) + 1):
        cases.append(list(itertools.permutations(numbers, r)))

    cases = list(set([int("".join(y)) for x in cases for y in x]))

    print(cases)

    for num in cases:
        if isPrime(num):
            answer += 1

    return answer


solution("011")
