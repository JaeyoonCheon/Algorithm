def compareGroup(A, B):
    if sum(A) > sum(B):
        return "left"
    elif sum(A) < sum(B):
        return "right"
    else:
        return "equal"


def weightedfakeCoinGroup(A, B, C, weight):
    """
    이 함수는 fake coin이 무겁다는 전제 하에 작성
    """
    result = compareGroup(A, B)
    if weight == "heavy":
        if result == "left":
            return A
        elif result == "right":
            return B
        else:
            return C
    else:
        if result == "left":
            return B
        elif result == "right":
            return A
        else:
            return C


def fakeCoinGroup(A, B, C):
    """
    이 함수는 2단계 비교를 통해 fake coin이 무거운 지 가벼운 지 구별
    """
    result = compareGroup(A, B)
    weight = ""
    fakeGroup = []

    if result == "left":
        result2 = compareGroup(A, C)
        if result2 == "left":
            weight = "heavy"
            fakeGroup = A
        else:
            weight = "light"
            fakeGroup = B
    elif result == "right":
        result2 = compareGroup(B, C)
        if result2 == "left":
            weight = "heavy"
            fakeGroup = B
        else:
            weight = "light"
            fakeGroup = A
    else:
        result2 = compareGroup(C, A)
        if result2 == "left":
            weight = "heavy"
            fakeGroup = C
        else:
            weight = "light"
            fakeGroup = C

    return fakeGroup, weight


def splitCoinGroup(list):
    """
    input으로 들어오는 리스트를 3개로 쪼개 반환
    몫을 기준으로 3개로 분할하므로, 전체 input값은 3^n개가 되어야 정상 작동
    """
    length = len(list)

    group1 = list[0 : length // 3]
    group2 = list[length // 3 : 2 * (length // 3)]
    group3 = list[2 * (length // 3) : length]

    return group1, group2, group3


def balancing(list):
    compared = 0
    currList = list

    group1, group2, group3 = splitCoinGroup(currList)
    currList, weight = fakeCoinGroup(group1, group2, group3)
    compared += 2
    while len(currList) > 1:
        group1, group2, group3 = splitCoinGroup(currList)
        currList = weightedfakeCoinGroup(group1, group2, group3, weight)
        compared += 1

    fakeCoin = currList[0]
    fakeCoinIdx = list.index(fakeCoin)

    return fakeCoin, fakeCoinIdx, compared


coinList = [
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    5,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
]

fakeCoin, fakeCoinIdx, compared = balancing(coinList)

print("The fake coin is", fakeCoin, " at", fakeCoinIdx, "in coinList")
print(compared, "compared")
