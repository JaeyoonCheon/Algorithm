import math


def getData(rec):
    hour, minute = int(rec[:2]), int(rec[3:5])
    number = rec[6:10]
    move = rec[11:]

    return (hour, minute, number, move)


def calculateFee(time, feeTable):
    baseTime, baseFee, unitTime, unitFee = (
        feeTable[0],
        feeTable[1],
        feeTable[2],
        feeTable[3],
    )

    if time <= baseTime:
        return baseFee
    else:
        return baseFee + math.ceil((time - baseTime) / unitTime) * unitFee


def solution(fees, records):
    answer = []

    cars = set([])
    carTime = {}
    carDict = {}

    for rec in records:
        data = getData(rec)
        hour, minute, number, move = data[0], data[1], data[2], data[3]

        if move == "IN":
            carDict[number] = [hour * 60 + minute]
        else:
            inTime = carDict[number].pop()

            if number in cars:
                carTime[number] += hour * 60 + minute - inTime
            else:
                cars.add(number)
                carTime[number] = hour * 60 + minute - inTime

    for number, carRec in carDict.items():
        if carRec:
            inTime = carDict[number].pop()

            if number in cars:
                carTime[number] += 23 * 60 + 59 - inTime
            else:
                cars.add(number)
                carTime[number] = 23 * 60 + 59 - inTime

    cars = sorted(list(cars))

    for car in cars:
        fee = calculateFee(carTime[car], fees)
        answer.append(fee)

    return answer


fees = [180, 5000, 10, 600]
records = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
]

print(solution(fees, records))
