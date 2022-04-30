"""
4153번 직각삼각형

1.  기본적인 피타고라스 공식 응용 문제
"""

while True:
    A, B, C = map(int, input().split())

    if A == 0 and B == 0 and C == 0:
        break

    slide = max(A, B, C)

    if slide == A:
        if pow(slide, 2) == pow(B, 2) + pow(C, 2):
            print("right")
        else:
            print("wrong")
    elif slide == B:
        if pow(slide, 2) == pow(A, 2) + pow(C, 2):
            print("right")
        else:
            print("wrong")
    else:
        if pow(slide, 2) == pow(A, 2) + pow(B, 2):
            print("right")
        else:
            print("wrong")
