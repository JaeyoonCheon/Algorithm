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

        tempCombination = []
        for i in combination:
            tempCombination.append(i[0])

        for j in dislikePairs:
            if j[0] in tempCombination and j[1] in tempCombination:
                good = False

        if good:
            like = inviteLike = 0
            for i in combination:
                like += i[1]
            for i in invite:
                inviteLike += i[1]
            if like > inviteLike:
                invite = combination
    return invite


list = [("A", 2), ("B", 6), ("C", 3), ("D", 10), ("E", 3)]
dislikePairs = [["A", "B"], ["B", "E"]]

print(inviteOptimized(list, dislikePairs))
