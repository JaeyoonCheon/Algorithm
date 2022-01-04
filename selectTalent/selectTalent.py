def best(combination, candidate, candidateTalent, talent):
    for t in talent:
        cover = False
        for c in combination:
            eachTalent = candidateTalent[candidate.index(c)]
            if t in eachTalent:
                cover = True
        if not cover:
            return False
    return True


def makeCombination(talent, candidate, candidateTalent):
    """
    make best covering combination in candidate-talent 2d sheet
    """
    n = len(candidate)
    pick = candidate[:]

    for i in range(pow(2, n)):
        num = i
        combination = []
        for j in range(n):
            if num % 2 == 1:
                combination = [candidate[n - j - 1]] + combination
            num = num // 2
        if best(combination, candidate, candidateTalent, talent):
            if len(pick) > len(combination):
                pick = combination
    return pick


def removeDuplicated(talent, candidate, candidateTalent):
    for i, v in enumerate(candidateTalent):
        for j in range(i + 1, len(candidateTalent)):
            if set(v) & set(candidateTalent[j]) == set(v):
                candidate.pop(i)
                candidateTalent.pop(i)
            if set(v) & set(candidateTalent[j]) == set(candidateTalent[j]):
                candidate.pop(j)
                candidateTalent.pop(j)

    return candidate, candidateTalent


def makeCombinationOptimized(talent, candidate, candidateTalent):
    candidate, candidateTalent = removeDuplicated(talent, candidate, candidateTalent)

    n = len(candidate)
    pick = candidate[:]

    for i in range(pow(2, n)):
        num = i
        combination = []
        for j in range(n):
            if num % 2 == 1:
                combination = [candidate[n - j - 1]] + combination
            num = num // 2
        if best(combination, candidate, candidateTalent, talent):
            if len(pick) > len(combination):
                pick = combination
    return pick


def selectUniqueTalent(talent, candidate, candidateTalent):
    uniqueCandidate = []
    for t in talent:
        count = 0
        idx = -1
        for i in candidateTalent:
            if t in i:
                count += 1
                idx = candidateTalent.index(i)
        if count == 1:
            uniqueCandidate.append(candidate[idx])
            talent.remove(t)

    return uniqueCandidate, talent


def makeCombinationOptimized2(talent, candidate, candidateTalent):
    uniqueCandidate, talent = selectUniqueTalent(talent, candidate, candidateTalent)

    for i in uniqueCandidate:
        candidateTalent.pop(candidate.index(i))
    candidate = list(set(candidate) - set(uniqueCandidate))
    candidate.sort()

    n = len(candidate)
    pick = candidate[:]

    for i in range(pow(2, n)):
        num = i
        combination = []
        for j in range(n):
            if num % 2 == 1:
                combination = [candidate[n - j - 1]] + combination
            num = num // 2
        if best(combination, candidate, candidateTalent, talent):
            if len(pick) > len(combination):
                pick = combination

    pick = list(set(pick) | set(uniqueCandidate))
    pick.sort()

    return pick


talent = ["Sing", "Dance", "Magic", "Act", "Flex", "Code"]
candidate = ["Aly", "Bob", "Cal", "Don", "Eve", "Fay"]
candidateTalents = [
    ["Flex", "Code"],
    ["Dance", "Magic"],
    ["Sing", "Magic"],
    ["Sing", "Dance"],
    ["Dance", "Act", "Code"],
    ["Act", "Code"],
]

print(makeCombination(talent, candidate, candidateTalents))
print(makeCombinationOptimized(talent, candidate.copy(), candidateTalents.copy()))
print(makeCombinationOptimized2(talent, candidate, candidateTalents))
