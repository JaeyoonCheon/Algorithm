def makeCombination(n, list):
    """
    참가자의 수 만큼의 자릿수를 가진 이진 비트열로 조합 표현
    """
    combination = []

    """
    000..000~111...111 사이의 수에서 
    각 자리수의 1과 참가자를 매칭시켜 모든 조합의 경우를 저장
    """
    for i in range(pow(2, n)):
        num = i
        cList = []
        for j in range(n):
            if num % 2 == 1:
                cList = [list[n - 1 - j]] + cList
            num = num // 2
        combination.append(cList)
    return combination


def removeBadCombinations(combination, dislikePairs):
    goodCombiantions = []

    for i in combination:
        good = True
        for j in dislikePairs:
            if j[0] in i and j[1] in i:
                good = False
        if good:
            goodCombiantions.append(i)
    return goodCombiantions


def invite(list, dislikePairs):
    combination = makeCombination(len(list), list)
    goodCombination = removeBadCombinations(combination, dislikePairs)

    maxInvite = []
    for i in goodCombination:
        if len(i) > len(maxInvite):
            maxInvite = i

    return maxInvite


def inviteOptimized(list, dislikePairs):
    """
    위 3개 함수를 통합하면서 가능한 조합의 경우를 저장하지 않고
    바로 크기 비교를 진행하여 메모리 공간 절약
    """
    n, invite = len(list), []

    for i in range(pow(2, n)):
        combination = []
        num = i
        for j in range(n):
            if num % 2 == 1:
                combination = [list[n - 1 - j]] + combination
            num = num // 2
        good = True
        for j in dislikePairs:
            if j[0] in combination and j[1] in combination:
                good = False
        if good:
            if len(combination) > len(invite):
                invite = combination
    return invite


def inviteOptimized2(invitelist, dislikePairs):
    """
    위 3개 함수를 통합하면서 가능한 조합의 경우를 저장하지 않고
    바로 크기 비교를 진행하여 메모리 공간 절약
    """
    invite = []
    always = invitelist.copy()

    for i in dislikePairs:
        if i[0] in always:
            always.remove(i[0])
        if i[1] in always:
            always.remove(i[1])

    invitelist = list(set(invitelist) - set(always))
    n = len(invitelist)

    for i in range(pow(2, n)):
        combination = []
        num = i
        for j in range(n):
            if num % 2 == 1:
                combination = [invitelist[n - 1 - j]] + combination
            num = num // 2
        good = True
        for j in dislikePairs:
            if j[0] in combination and j[1] in combination:
                good = False
        if good:
            if len(combination) > len(invite):
                invite = combination

    invite = list(set(invite) | set(always))
    invite.sort()

    return invite


invitelist = ["A", "B", "C", "D", "E"]
largeList = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
dislikePairs = [["A", "B"], ["B", "C"]]
largeDislikePairs = [
    ["B", "C"],
    ["C", "D"],
    ["D", "E"],
    ["F", "G"],
    ["F", "H"],
    ["F", "I"],
    ["G", "H"],
]
print(invite(largeList, largeDislikePairs))
print(inviteOptimized(largeList, largeDislikePairs))
print(inviteOptimized2(largeList, largeDislikePairs))
