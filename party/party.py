def bruteFindMaxParticipant(schedule):
    startParty = schedule[0][0]
    endParty = schedule[0][1]

    for i in range(1, len(schedule)):
        startParty = min(schedule[i][0], startParty)
        endParty = max(schedule[i][1], endParty)

    maxParticipant = 0
    maxTime = 0
    for i in range(startParty, endParty):
        count = 0
        for j in schedule:
            if j[0] <= i and j[1] > i:
                count = count + 1
        if maxParticipant < count:
            maxParticipant = count
            maxTime = i

    return (maxParticipant, maxTime)


def sortSchedule(schedule):
    """
    selection sort
    """
    for i in range(len(schedule) - 1):
        minIdx = i
        for j in range(i, len(schedule)):
            if schedule[j][0] < schedule[minIdx][0]:
                minIdx = j
        schedule[i], schedule[minIdx] = schedule[minIdx], schedule[i]


def findMaxParticipant(schedule):
    timeline = []
    for i in schedule:
        timeline.append((i[0], "start"))
        timeline.append((i[1], "end"))

    sortSchedule(timeline)

    currParticipant = 0
    maxTime = maxParticipant = 0
    for i in timeline:
        if i[1] == "start":
            currParticipant = currParticipant + 1
        if i[1] == "end":
            currParticipant = currParticipant - 1
        if currParticipant > maxParticipant:
            maxParticipant = currParticipant
            maxTime = i[0]

    return (maxParticipant, maxTime)


schedule = [
    (6, 8),
    (6, 12),
    (9, 10),
    (6, 7),
    (7, 8),
    (7, 10),
    (8, 9),
    (8, 10),
    (9, 12),
    (10, 11),
    (10, 12),
    (11, 12),
]

print(
    bruteFindMaxParticipant(schedule)[1],
    "'O clock,",
    bruteFindMaxParticipant(schedule)[0],
    "people",
)

print(
    findMaxParticipant(schedule)[1], "'O clock,", findMaxParticipant(schedule)[0], "people",
)
