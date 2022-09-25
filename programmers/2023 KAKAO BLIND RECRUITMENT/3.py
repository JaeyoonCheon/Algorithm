def check(users, emo):
    participant, sales = 0, 0

    for user in users:
        totalVal = 0
        wanaDc, maxVal = user[0], user[1]
        isPlusUser = False

        for e in emo:
            dc, val = e[0], e[1]

            if dc * 10 >= wanaDc:
                totalVal += val

            if maxVal <= totalVal:
                isPlusUser = True
                break

        if isPlusUser:
            participant += 1
        else:
            sales += totalVal

    return (participant, sales)


def solution(users, emoticons):
    maxUser = 0
    maxValue = 0

    def dfs(idx, pEmo):
        nonlocal users
        nonlocal emoticons
        nonlocal maxUser
        nonlocal maxValue

        if idx == len(emoticons):
            result = check(users, pEmo)
            if result[0] > maxUser:
                maxUser = result[0]
                maxValue = result[1]
            elif result[0] == maxUser and result[1] > maxValue:
                maxValue = result[1]
            else:
                pass

            return

        for i in range(1, 5):
            pEmo.append((i, int(emoticons[idx] * ((10 - i) / 10))))
            dfs(idx + 1, pEmo)
            pEmo.pop()

    answer = []

    dfs(0, [])

    answer.append(maxUser)
    answer.append(maxValue)

    return answer


tUser1 = [[40, 10000], [25, 10000]]
tEmo1 = [7000, 9000]

tUser2 = [
    [40, 2900],
    [23, 10000],
    [11, 5200],
    [5, 5900],
    [40, 3100],
    [27, 9200],
    [32, 6900],
]
tEmo2 = [1300, 1500, 1600, 4900]

tUser3 = [[1, 11000]]
tEmo3 = [10000]


print(solution(tUser3, tEmo3))
