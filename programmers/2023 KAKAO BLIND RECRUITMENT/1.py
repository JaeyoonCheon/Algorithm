MONTH = 28


def parsing(time):
    year = time[2:4]
    month = time[5:7]
    day = time[8:10]

    return 12 * MONTH * int(year) + MONTH * int(month) + int(day)


def solution(today, terms, privacies):
    answer = []

    todayDate = parsing(today)

    termsDict = {}

    for term in terms:
        datatype, period = term.split()
        period = int(period)

        termsDict[datatype] = period

    for idx, privacy in enumerate(privacies):
        date, datatype = privacy.split()

        privDate = parsing(date)

        if todayDate - privDate >= termsDict[datatype] * MONTH:
            answer.append(idx + 1)

    return answer


solution()
