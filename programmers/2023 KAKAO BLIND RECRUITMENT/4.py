import math


def check(number, _from, _to):
    mid = (_to + _from) // 2

    if _to == _from:
        return True

    if number & (1 << mid) == 0:
        return False
    else:
        return check(number, _from, mid - 1) and check(number, mid + 1, _to)


def isPowerOf2(n):
    return (n & (n - 1)) == 0


def solution(numbers):
    answer = []

    for number in numbers:
        logedNumber = math.floor(math.log(number, 2))
        # length = len(bin(number)[2:])
        threshold = pow(2, math.ceil(math.log(logedNumber + 1, 2))) - 1
        # threshold = pow(2, math.ceil(math.log(length, 2))) - 1

        if number > 1:
            if check(number, 0, threshold - 1):
                answer.append(1)
            else:
                answer.append(0)
        else:
            answer.append(0)

    return answer


test1 = [7, 5]
test2 = [63, 111, 95]

print(solution(test1))
