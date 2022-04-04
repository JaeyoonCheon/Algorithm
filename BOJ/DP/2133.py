"""
2133번 타일 채우기

1.  재귀 이용한 풀이법을 적용.

2.  우선, 유사한 문제와 같이 최소 부분 단위를 탐색해보았다.
    1*2, 2*1타일을 가지고 3*N타일을 채우기 위해 나타나는 반복적인 최소 단위는
    가로 2칸 범위에서 3가지가 나타났다.

3.  가로 폭이 홀수일 경우에는 물리적으로 알맞게 덮을 수 있는 경우의 수가 존재하지 않으므로,
    짝수인 경우만 고려해서 풀이하였는데, 가로 폭 4인 경우 만들 수 있는 경우의 수는 가로 폭 2인 경우를
    조합해서 만들 수 있는 경우 7가지와, 가로 폭 4인 경우에 나타나는 유일한 조합의 경우 2가지의 합인 9가지이다.
    
4.  이후, 가로 폭이 6, 8, 10... 인 경우를 생각해 보면, 이전 경우의 조합 + 새로 만들어지는 경우 2가지를 합한
    조합의 경우의 수가 나타난다는 것을 알게 되었다.
    따라서, 점화식은 3*tiling(N-2) + 2*tiling(N-4) + 2*tiling(N-6)...으로 나타난다.
"""

N = int(input())


def tiling(N):
    if N == 0:
        return 1
    elif N < 0:
        return 0
    else:
        sum = 0
        if N > 1:
            for i in range(2, N + 1, 2):
                if i == 2:
                    sum += 3 * tiling(N - i)
                    continue
                sum += 2 * tiling(N - i)
        return sum


print(tiling(N))
