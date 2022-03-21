"""
11727번 2xn 타일링 2

1.  11726번과 같이 동작하나, 가로 2칸을 놓는 방법이 1x2타일을 2개놓는 방법과 2x2타일을 놓는 방법
    2가지가 있다. 1x2 타일 2개를 놓는 방법은 2x2타일 하나를 놓는 방법으로 대체 가능하므로,
    결과적으로 가로 2칸을 채우는 방법이 2배가 된다.
    따라서 점화식은 tiling(n-1) + tiling(n-2) * 2가 된다.
    
2.  이 문제는 top-down 뿐만 아니라 bottom-up으로도 접근 가능하다.
    기본으로 0칸, 1칸, 2칸을 채우는 경우의 수를 가지고 3칸, 4칸, n칸 까지
    경우의 수를 조합해 나가는 방식으로 이 경우에도 가로 2칸을 채우는 경우의 수가 2배가 되므로
    이것을 고려해 n까지 올라가면서 채운다.
"""

from numpy import number


cache = [-1] * 1001


def tiling(n):
    if cache[n] != -1:
        return cache[n]
    if n == 0:
        return 1
    case2 = 0
    if n > 1:
        case2 = tiling(n - 2)

    cache[n] = tiling(n - 1) + case2 * 2

    return cache[n]


n = int(input())

print(tiling(n) % 10007)

li = [0, 1, 3]

for i in range(3, n + 1):
    li.append(li[i - 1] + li[i - 2] * 2)

print(li[n] % 10007)
