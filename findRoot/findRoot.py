def simpleFindSquareRoot(x):
    ans = 0

    if x < 0:
        print("no imaginary numbers")
        return

    while pow(ans, 2) < x:
        ans += 1

    if pow(ans, 2) != x:
        print(x, "is not square number")
        print("square root of", x, "is close to", ans - 1)
    else:
        print("square root of", x, "is", ans)


def simpleFindSquareRootWithError(x, e, increment):
    ans = 0.0
    numGuesses = 0

    if x < 0:
        print("no imaginary numbers")
        return

    while x - pow(ans, 2) > e:
        ans += increment
        numGuesses += 1

    print("numGuesses =", numGuesses)

    if abs(pow(ans, 2) - x) > e:
        print("Failed on square root of", x)
    else:
        print(ans, "is close to square root of", x)


def bisearchSquareRoot(x, e):
    numGuesses = 0
    lo = 0.0
    hi = x
    if 0 < x < 1:
        ans = (lo + hi) * 2.0
    else:
        ans = (lo + hi) / 2.0

    if x < 0:
        print("no imaginary numbers")
        return

    while abs(pow(ans, 2) - x) >= e:
        if pow(ans, 2) < x:
            lo = ans
        else:
            hi = ans

        if 0 < x < 1:
            ans = (lo + hi) * 2.0
        else:
            ans = (lo + hi) / 2.0
        numGuesses += 1

    print("numGuesses =", numGuesses)
    print(ans, "is close to square root of", x)


number = 0.2
# simpleFindSquareRoot(number)
# simpleFindSquareRootWithError(number, 0.01, 0.00001)
bisearchSquareRoot(number, 0.01)
