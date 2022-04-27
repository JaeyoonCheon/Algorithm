"""
1929번 소수 구하기

1.  소수 -> 에라토스테네스의 체 사용

2.  에라토스테네스의 체
    2부터 시작하여 그 수의 배수들을 모두 지워나가 원하는 숫자 N까지 반복하면
    2~N까지의 소수만 남길 수 있다.
    
3.  이 문제에서 백만 번의 검사를 수행해야 하기 때문에, 소수라고 판별되면 바로 출력하는 것이
    시간 상 효율적일 것이다.
"""


def erathos(lower, upper):
    numbers = [True] * 10000001

    for i in range(2, upper + 1):
        if numbers[i] == False:
            continue
        else:
            if i <= upper and i >= lower:
                print(i)
            j = 2
            while i * j <= upper:
                numbers[i * j] = False
                j += 1

    return numbers


M, N = map(int, input().split())

erathos(M, N)
