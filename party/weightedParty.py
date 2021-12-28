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


def weightedParticipant(schedule):
    timeline = []
    for i in schedule:
        timeline.append((i[0], i[2], "start"))
        timeline.append((i[1], i[2], "end"))

    sortSchedule(timeline)

    currWeight = 0
    maxTime = maxWeight = 0
    for i in timeline:
        if i[2] == "start":
            currWeight = currWeight + i[1]
        if i[2] == "end":
            currWeight = currWeight - i[1]
        if currWeight > maxWeight:
            maxWeight = currWeight
            maxTime = i[0]

    return (maxWeight, maxTime)


weightedSchedule = [
    (6.0, 8.0, 2),
    (6.0, 12.0, 1),
    (6.5, 7.0, 2),
    (7.0, 8.0, 2),
    (7.5, 10.0, 3),
    (8.0, 9.0, 2),
    (8.0, 10.0, 1),
    (9.0, 12.0, 2),
    (9.5, 10.0, 4),
    (10.0, 11.0, 2),
    (10.0, 12.0, 3),
    (11.0, 12.0, 7),
]

print(
    weightedParticipant(weightedSchedule)[1],
    "'O clock,",
    weightedParticipant(weightedSchedule)[0],
    "preference",
)
