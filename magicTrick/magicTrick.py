import random as rd


def distance(pair):
    number = []
    firstCard = 0
    targetCard = 0

    for i in pair:
        number.append((int(i[1] / 4), i[0]))

    dist = (number[0][0] - number[1][0]) % 13

    if dist > 0 and dist <= 6:
        targetCard = pair[0]
        firstCard = pair[1]
    else:
        targetCard = pair[1]
        firstCard = pair[0]
        dist = (number[1][0] - number[0][0]) % 13

    return targetCard, firstCard, dist


def encoding(remain, selected, dist):
    remain = sorted(remain, key=lambda remain: remain[1])
    cardSeq = []
    if dist == 1:
        cardSeq.append(remain[0])
        cardSeq.append(remain[1])
        cardSeq.append(remain[2])
    elif dist == 2:
        cardSeq.append(remain[0])
        cardSeq.append(remain[2])
        cardSeq.append(remain[1])
    elif dist == 3:
        cardSeq.append(remain[1])
        cardSeq.append(remain[0])
        cardSeq.append(remain[2])
    elif dist == 4:
        cardSeq.append(remain[1])
        cardSeq.append(remain[2])
        cardSeq.append(remain[0])
    elif dist == 5:
        cardSeq.append(remain[2])
        cardSeq.append(remain[0])
        cardSeq.append(remain[1])
    else:
        cardSeq.append(remain[2])
        cardSeq.append(remain[1])
        cardSeq.append(remain[0])

    return cardSeq


def assistant(deck):
    selected = []
    symbolList = []
    pair = []
    cardSeq = []
    remain = []

    while len(selected) < 5:
        pick = rd.randint(0, 51)
        dup = False
        for element in selected:
            if pick == element[1]:
                dup = True
        if dup != True:
            symbol = pick % 4
            selected.append((deck[pick], pick, symbol))
        else:
            continue
        for i, v in enumerate(symbolList):
            if v == symbol:
                pair.append(selected[i])
                pair.append((deck[pick], pick, symbol))
                break
        symbolList.append(symbol)

    temp = set(pair)
    pair = list(temp)
    pair = sorted(pair, key=lambda pair: pair[2])
    targetCard, firstCard, dist = distance(pair)

    cardSeq.append(firstCard)

    for i in selected:
        if i != targetCard and i != firstCard:
            remain.append(i)

    cardSeq.extend(encoding(remain, selected, dist))

    print("shown four cards are", cardSeq)
    print("hidden card is", targetCard)
    print("encoding is", dist)

    return cardSeq


def magician(cardSec, deck):
    firstCard = cardSec[0]
    targetSymbol = firstCard[2]

    decoding = 0
    if cardSec[1][1] < cardSec[2][1] < cardSec[3][1]:
        decoding = 1
    elif cardSec[1][1] < cardSec[3][1] < cardSec[2][1]:
        decoding = 2
    elif cardSec[2][1] < cardSec[1][1] < cardSec[3][1]:
        decoding = 3
    elif cardSec[2][1] < cardSec[3][1] < cardSec[2][1]:
        decoding = 5
    elif cardSec[3][1] < cardSec[1][1] < cardSec[2][1]:
        decoding = 4
    elif cardSec[3][1] < cardSec[2][1] < cardSec[1][1]:
        decoding = 6
    else:
        decoding = 0

    targetNumber = (decoding + firstCard[1] // 4) % 13
    targetIdx = targetNumber * 4 + targetSymbol
    targetCard = (deck[targetIdx], targetIdx, targetSymbol)

    print("decoding is", decoding)
    print("magician : hidden card is ", targetCard)


deck = [
    "A_C",
    "A_D",
    "A_H",
    "A_S",
    "2_C",
    "2_D",
    "2_H",
    "2_S",
    "3_C",
    "3_D",
    "3_H",
    "3_S",
    "4_C",
    "4_D",
    "4_H",
    "4_S",
    "5_C",
    "5_D",
    "5_H",
    "5_S",
    "6_C",
    "6_D",
    "6_H",
    "6_S",
    "7_C",
    "7_D",
    "7_H",
    "7_S",
    "8_C",
    "8_D",
    "8_H",
    "8_S",
    "9_C",
    "9_D",
    "9_H",
    "9_S",
    "10_C",
    "10_D",
    "10_H",
    "10_S",
    "J_C",
    "J_D",
    "J_H",
    "J_S",
    "Q_C",
    "Q_D",
    "Q_H",
    "Q_S",
    "K_C",
    "K_D",
    "K_H",
    "K_S",
]

cardSec = assistant(deck)
magician(cardSec, deck)
