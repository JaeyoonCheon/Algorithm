"""
2309 일곱 난쟁이

9명의 난쟁이 중 난쟁이가 아닌 2명을 골라낸 경우를 찾는것이므로,
9명 중 2명을 제한 모든 경우에 대해 키의 합이 100인지 확인
"""

from functools import reduce


def exam(height):
    height.sort()
    for i in range(9):
        first = height.pop(i)
        for j in range(8):
            second = height.pop(j)
            if reduce(lambda x, y: x + y, height) == 100:
                return height
            height.append(second)
            height.sort()
        height.append(first)
        height.sort()


height = [int(input()) for _ in range(9)]
result = exam(height)
result.sort()
for i in result:
    print(i)
