def erathos(N):
    numbers = [False] * (N + 1)
    numbers[0], numbers[1] = True, True
    for i in range(2, N // 2):
        if not numbers[i]:
            j = 2
            while i * j <= N:
                numbers[i * j] = True
                j += 1

    return numbers


def translation(N, K):
    temp = ""

    while N > 0:
        N, M = N // K, N % K
        temp += str(M)

    temp = "".join(reversed(temp))

    return temp


def solution(n, k):
    answer = -1

    conversion = translation(n, k)
    cand = conversion.replace("0", " ")
    cand = cand.split()

    candint = list(map(int, cand))

    maxNumber = max(candint)

    prime = erathos(maxNumber + 1)

    count = 0

    for i in candint:
        if not prime[i]:
            count += 1

    answer = count

    return answer


print(solution(437674, 3))
