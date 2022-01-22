def counting(cases):
    total = 0

    N = max(cases)

    for i in range(1, N + 1):
        total += i * int(N / i)
        if i in cases:
            print(total)
    return total


iter = int(input())

cases = []

for _ in range(iter):
    cases.append(int(input()))

counting(cases)
