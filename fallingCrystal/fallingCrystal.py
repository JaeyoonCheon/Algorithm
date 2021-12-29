def convertToDec(floor, radix):
    decimal = 0
    for i in range(len(floor)):
        decimal = decimal + floor[i] * pow(radix, i + 1)

    return decimal


def fallingCrystal(n, d, threshold):
    r = 1
    while pow(r, d) <= n:
        r = r + 1

    count = 0
    floor = [0] * d

    for i in range(d):
        for j in range(r - 1):
            a = 1


test = [0, 1, 0, 0]
radix = 2

print(convertToDec(test, radix))
