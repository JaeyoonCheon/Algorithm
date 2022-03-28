"""
1699번 제곱수의 합

1.  어떤 자연수 N을 어떤 자연수 a, b, c 등의 제곱으로 나타낸 것이 제곱수
    따라서, 생각해볼 수 있는 것은 DP의 단위를 N보다 작은 어떤 제곱수를 뺀 것의 정보를
    저장해 놓고 가져 올 수 있는 것
    
2.  기저조건으로 1, 4, 9 등의 제곱인 수의 인덱스를 1로 설정해 놓는다
    * 이 조건을 제외해도 1위치만 1로 설정해 놓는다면 다른 수는 자연스럽게 이후의 점화식에 의해
    처리되므로 제거해도 무방
    
3.  2 ~ N 사이의 수를 순회하며 수를 선택
    이후, 해당 수에서 제곱수를 차감하며 남은 수를 저장한 데이터를 불러와야 하므로,
    1~root(i) 사이에서의 수를 제곱하여 해당 수에서 빼면서 1을 더한(그 제곱인 수를 사용)것 cache[i - pow(j, 2)] + 1과
    그 제곱수를 사용하지 않은 구해놓은 cache[i]를 비교하여 더 작은 것을 택한다.
    
4.  이 방법 하에서는 pypy3는 통과하나, python3는 시간초과로 통과하지 못한다.
    이중 for문 내부에서 계속해서 1)제곱을 구하고 2)범위를 구할 때 import한 모듈 사용 3)제곱의 방법을 pow모듈 사용
    등의 사유로 최적화를 시켜야 가능할 것으로 생각된다.
"""

import math

N = int(input())

cache = [100001] * (N + 1)
cache[0] = 0

for i in range(1, math.floor(math.sqrt(N)) + 1):
    cache[pow(i, 2)] = 1

for i in range(2, N + 1):
    for j in range(1, math.floor(math.sqrt(i)) + 1):
        if pow(j, 2) > i:
            continue
        if cache[i] > cache[i - pow(j, 2)] + 1:
            cache[i] = cache[i - pow(j, 2)] + 1

print(cache[N])
