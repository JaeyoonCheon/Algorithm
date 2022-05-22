"""
1676번 팩토리얼 0의 개수

1.  N!을 구한 뒤 문자열로 변환하고 뒤집어 0을 센다.
"""

import math

N = int(input())

factN = math.factorial(N)

digits = list(str(factN))
digits.reverse()

count = 0

for i in range(len(digits)):
    if digits[i] != "0":
        break
    else:
        count += 1

print(count)
