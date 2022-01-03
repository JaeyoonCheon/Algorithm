def convertToDec(floor, radix):
    decimal = 0
    for i in range(len(floor)):
        decimal = decimal + floor[i] * pow(radix, len(floor) - i - 1)

    return decimal


def fallingCrystal(n, d, threshold):
    """
    n개의 구슬을 떨어뜨릴 수 있을 경우,
    전체 층을 k구간으로 분리할 경우 각 층은 1k, 2k, 3k, ..., (n/k-1)k, (n/k)k층에 위치하게 된다
    이 때 최악의 실험 반복 수를 가정해 보면 마지막 층에서 첫번째 구슬이 깨져 [(n/k-1)k+1, (n/k)k-1]구간에 대해
    두번째 구슬로 검사가 필요하다. 따라서, n/k + (k-1)번 검사하게 되므로 산술-기하 평균에 의해
    sqrt(n/k * k) = sqrt(n)이므로, k를 최소로 하는 구간은 k가 root n일 시점이다
    자릿수 표현을 응용하여, 구슬의 갯수가 자릿수, 나누는 구간 k는 root_d(n)으로 정해 숫자의 진수로 표현
    """
    r = 1
    while pow(r, d) <= n:
        r = r + 1

    count = 0
    floor = [0] * d

    for i in range(d):
        for j in range(r - 1):
            floor[i] = floor[i] + 1
            curr = convertToDec(floor, r)
            if curr > threshold:
                floor[i] = floor[i] - 1
                break

    print(floor)
    return convertToDec(floor, r)


N = 128
d = 6
threshold = 130
print("threshold is", threshold)
print(fallingCrystal(N, d, threshold))
