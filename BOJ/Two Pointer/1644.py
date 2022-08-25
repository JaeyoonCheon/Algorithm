"""
1644번 소수의 연속합

1.  기본적인 풀이 논리는 N까지의 소수들을 구한 뒤, 그 소수들 중 연속된 경우의 합이 N이 되는 경우를 세는 것이다.

2.  일단 처음에 에라토스테네스의 체 알고리즘을 통한 N까지의 소수를 구하였고, 반복문을 돌면서 prime[start:end]의 합이
    N이 되는 경우를 체크했다. 하지만 이 경우 sum(prime[start:end])가 매번 합계를 계산해야 하므로 비효율적이었고,
    소수를 구할 때 4000000개 중 각각의 수가 소수인지 아닌지만 체크 후 따로 소수를 저장했기 때문에
    4백만번의 loop를 별도로 돌아야 하는 비효율이 있었다.

3.  따라서, 계산 중 소수를 조우할 시 바로 primeNumber 리스트에 추가하도록 변경했고
    투 포인터를 사용해 하나의 합계에서 양 끝만 변동되도록 개선하여 효율적인 알고리즘을 구성했다.
"""

N = int(input())


def erathos(N):
    isPrimeNumber = [True] * (N + 1)
    primeNumber = []

    isPrimeNumber[0], isPrimeNumber[1] = False, False
    for number in range(2, N + 1):
        if isPrimeNumber[number]:
            primeNumber.append(number)
            for i in range(2, N):
                if number * i > N:
                    break
                isPrimeNumber[number * i] = False

    return primeNumber


def checkSum(N):
    prime = erathos(N)
    count = 0
    length = len(prime)

    start, end = 0, 0

    for end in range(length):
        sum = prime[end]
        if sum == N:
            count += 1
            continue
        else:
            for start in range(end - 1, -1, -1):
                sum += prime[start]
                if sum == N:
                    count += 1
                    break
                if sum > N:
                    break
    print(count)


checkSum(N)
