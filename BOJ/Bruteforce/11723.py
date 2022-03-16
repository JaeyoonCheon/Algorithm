"""
11723번 집합

1.  문제 조건을 보면 1,5초와 4MB 메모리 제한 내에 최대 3백만 번의 연산을 수행해야 한다.
    이 때, 일반적인 list형태로 연산을 저장하고 인덱스에 접근하기 위해서는 너무 많은 탐색 시간과
    낭비되는 메모리 공간이 발생한다.
2.  입력되는 x의 값은 1 ~ 20 사이의 정수로 한정되기 때문에, 
    00000000000000000000 ~ 11111111111111111111로 표현되는 2진수 비트마스크로 집합 S를 간주하자.
3.  add는 원하는 수만큼 시프트한 비트와 집합 S의 OR연산, remove는 원하는 수만큼 시프트한 비트를 NOT연산 후 AND연산.
    check는 원하는 수만큼 시프트한 비트와 AND연산을 한 뒤 양수인지 체크하여 파악
    
*   파이썬 입력으로 사용하는 input() 메소드는 느리기 때문에,
    버퍼를 사용하는 sys.stdin.readline()을 사용해야 python3로 통과 가능하다.
"""

import sys

M = int(input())

S = 0

for i in range(M):
    instructions = [i for i in sys.stdin.readline().split()]
    op = instructions[0]

    try:
        num = instructions[1]
        num = int(num)
    except:
        pass

    if op == "add":
        S = S | (1 << num)
    elif op == "remove":
        S = S & ~(1 << num)
    elif op == "check":
        temp = S & (1 << num)
        if temp > 0:
            print("1")
        else:
            print("0")
    elif op == "toggle":
        temp = S & (1 << num)
        if temp > 0:
            S = S & ~(1 << num)
        else:
            S = S | (1 << num)
    elif op == "all":
        S = pow(2, 21) - 1
    else:
        S = 0
