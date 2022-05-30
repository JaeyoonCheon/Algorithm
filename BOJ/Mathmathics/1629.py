"""
1629번 곱셈

1.  A의 B거듭제곱을 1초 안에 계산해 C로 나눈 값을 구하는 문제이다.
    A, B는 정수 한계값까지의 범위를 가지기 때문에, 거듭제곱 과정에서
    정수 한계를 넘겨 메모리 초과를 만들어 버린다.
    따라서 계산 도중에 계속해서 C로 나누어 주어야하는데 너무 잦은 나머지 연산은
    시간 측면에서 좋지 않으므로, 효율적인 나머지 연산의 분배가 필요한 문제이다.
    
2.  가장 편하고 빠른 방법은 python 내장 메소드 중 pow의 매개변수로
    A, B, C를 넘기면 해당 수를 자동적으로 연산해 준다.
    
3.  재귀 / 반복법으로 구현한 거듭제곱 연산방법을 dynamic, power 함수에 작성했다.
    기본적인 아이디어는 지수 승을 이진수로 바라보면서 나타난 이진수의 자릿수가
    1이면 이전 자리수에서 구해진 값을 제곱해서 넘겨주고, 0이라면 이전 자리수에서 구해진 값에
    밑을 한번 더 곱한 값을 넘겨줌으로서 분할 정복을 응용해 값을 구할 수 있다.
"""

A, B, C = map(int, input().split())


def dynamic(base, exp):
    if exp == 1:
        return base % C
    elif exp % 2 == 0:
        partial = dynamic(base, exp // 2)
        return (partial * partial) % C
    else:
        partial = dynamic(base, (exp - 1) // 2)
        return (partial * partial * base) % C


def power():
    total = 1
    base, exp = A, B

    while exp:
        if exp & 1:
            total = (total * base) % C
        exp = exp // 2
        base = (base * base) % C

    print(total)


def powerMethod():
    print(pow(A, B, C))


print(dynamic(A, B))
