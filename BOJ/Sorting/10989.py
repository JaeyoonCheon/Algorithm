"""
10989번 수 정렬하기 3

1.  천만개의 수를 5초 안에 오름차순 정렬해야 하는 문제.
    우선 기본 파이썬 내장 정렬함수로 수행한 결과 메모리 초과 오류가 발생하였다.
    파이썬 내장함수는 Tim 정렬 기반으로, NlogN의 시간 복잡도와 추가 메모리를 필요로 한다.
    따라서, 해당 함수로 안된다는 것은 정렬 메소드 자체의 사용을 피해야 할 것으로 생각되었다.
    
2.  입출력 시간을 절약하기 위해, 입력과 동시에 정렬을 수행하려고 한다.
    또한 문제의 조건에서 수의 제한이 10000 이하의 자연수로 제한이 걸려 있으므로,
    10000크기의 배열에 입력받는 수의 갯수를 넣고 추후 출력만 하면 되는 간단한 문제로 바뀌게 된다.
"""

import sys

N = int(input())

numbers = [0] * 10001

for i in range(N):
    numbers[int(sys.stdin.readline())] += 1

for i, v in enumerate(numbers):
    if v != 0:
        for _ in range(v):
            print(i)
