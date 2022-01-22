def findMult(n):
    l = list(str(n))
    for i in l:
        if i != "1":
            return False
    return True


def bruteForce():
    """
    무식하게 1로 이루어진 배수가 나올 때 까지 1의 자리가 1인 모든 배수에 대해 체크
    """
    while True:
        try:
            n = int(input())
            result = False
            mult = 1
            while result == False:
                temp = n * mult
                if temp % 10 == 1:
                    result = findMult(temp)
                mult += 1

            print(temp)
            print(len(list(str(temp))))
        except EOFError:
            break


def reverse():
    """
    1로 이루어진 수들에 대해 n의 배수인지 체크하는 방식
    시간적인 면에서 bruteForce보다 훨씬 빠를 것
    """
    while True:
        try:
            n = int(input())
            result = False
            mult = 1
            while result == False:
                if mult % n == 0:
                    result = True
                else:
                    mult = mult * 10 + 1

            print(len(list(str(mult))))
        except EOFError:
            break


reverse()
