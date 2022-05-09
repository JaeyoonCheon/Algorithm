"""
15829번 Hashing

1.  해시 함수 구현

2.  모듈러 연산이 적용되어 있기 때문에, 각각의 항을 더할때도 MOD를 해주어야 하고
    최종 합에도 또한 MOD를 해 주어야 한다.
"""

M = 1234567891


def hasing(string):
    sum = 0
    for i, ch in enumerate(string):
        sum += ((ord(ch) - 96) * (31 ** i)) % M

    return sum % M


L = int(input())

string = input()

print(hasing(string))
