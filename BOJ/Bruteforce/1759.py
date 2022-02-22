"""
1759번 암호 만들기

1. 백트래킹 이용
C개의 후보군 중 L개의 문자를 조건에 맞게 중복 없이 골라야하는 문제
따라서, L 파라미터를 줄여가면서 재귀 백트래킹으로 경우를 탐색

2. 파이썬 ord 메소드는 c에서 문자의 아스키코드 숫자로 변환해주는 것과 동일.
따라서, 문자의 정렬 서순을 비교하기에 알맞은 방법

3. checkCondition 함수에서 만들어진 암호문의 자음/모음의 갯수를 확인, 조건에 맞는지 확인
"""


def checkCondition(crpyto):
    # 모음
    vow = ["a", "e", "i", "o", "u"]
    # 모음의 갯수
    vowCount = 0
    # 자음의 갯수
    consCount = 0

    for i in crpyto:
        if i not in vow:
            consCount += 1
        else:
            vowCount += 1

    if consCount < 2 or vowCount < 1:
        return False

    return True


def makeCrypto(alpha, crypto, L, C):
    if L == 0:
        if checkCondition(crpyto) == False:
            return
        else:
            print("".join(map(str, crypto)))
            return
    for i in range(C):
        flag = False
        if alpha[i] in crpyto:
            continue
        for j in crpyto:
            if ord(alpha[i]) < ord(j):
                flag = True
        if flag == True:
            continue

        crpyto.append(alpha[i])
        makeCrypto(alpha, crypto, L - 1, C)
        crpyto.pop()


L, C = map(int, input().split())

alpha = list(input().split())
alpha.sort()

crpyto = []

makeCrypto(alpha, crpyto, L, C)
