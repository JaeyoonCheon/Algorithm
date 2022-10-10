"""
2480번 주사위 세계
"""

numbers = list(map(int, input().split()))

rmDup = set(numbers)

case = len(rmDup)

if case == 1:
    print(10000 + numbers[0] * 1000)
if case == 2:
    A, B = rmDup.pop(), rmDup.pop()

    if numbers.count(A) > numbers.count(B):
        print(1000 + 100 * A)
    else:
        print(1000 + 100 * B)
if case == 3:
    print(100 * max(numbers))
