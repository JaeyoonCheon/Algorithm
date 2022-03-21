"""
11726번 2xn 타일링

1.  2xn 타일을 왼쪽에서부터 타일을 놓아 모두 채울 수 있는 방법은 두가지이다.
    1) 타일을 세로로 하나 놓아 가로 1칸을 채우는 방법
    2) 타일 2개를 가로로 놓아 가로 2칸을 채우는 방법
    
    tiling(n)은 2xn 타일에 놓을 수 있는 방법의 수라고 하면
    점화식은 tiling(n-1) + tiling(n-2)가 된다.
    
2.  메모이제이션 없이 순수 점화식으로는 1번 방법은 시간초과
    메모이제이션 적용 시 통과
"""

cache = [-1] * 1001


def tiling(n):
    if cache[n] != -1:
        return cache[n]
    case1 = 0
    if n == 0:
        return 1
    if n > 1:
        case1 = tiling(n - 2)

    cache[n] = tiling(n - 1) + case1
    return cache[n]


n = int(input())

cache[0] = 1

print(tiling(n) % 10007)
