"""
2231번 분해합

1.  완전탐색을 이용하여 어떤 수 i + i의 자리수 합이 N과 같아지는 처음 지점을 반환
"""

N = int(input())
isExist = False


def getDigit(number):
    sum = 0

    while number:
        sum += number % 10
        number = number // 10

    return sum


for i in range(1, N):
    if i + getDigit(i) == N:
        isExist = True
        print(i)
        break

if not isExist:
    print(0)
