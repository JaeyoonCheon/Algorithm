MAX_DIST = 100001


def solution(cap, n, deliveries, pickups):
    answer = 0

    while True:
        dCap = cap
        pCap = cap
        maxDelivery = MAX_DIST
        maxPickup = MAX_DIST

        for house in range(n - 1, -1, -1):
            if dCap == 0 and pCap == 0:
                break

            if deliveries[house] <= dCap and deliveries[house] > 0:
                if maxDelivery == MAX_DIST:
                    maxDelivery = house

                dCap -= deliveries[house]
                deliveries[house] = 0
            else:
                if dCap > 0 and deliveries[house] > 0:
                    if maxDelivery == MAX_DIST:
                        maxDelivery = house

                    deliveries[house] -= dCap
                    dCap = 0

            if pickups[house] <= pCap and pickups[house] > 0:
                if maxPickup == MAX_DIST:
                    maxPickup = house
                pCap -= pickups[house]
                pickups[house] = 0
            else:
                if pCap > 0 and pickups[house] > 0:
                    if maxPickup == MAX_DIST:
                        maxPickup = house
                    pickups[house] -= pCap
                    dCap = 0

        if maxDelivery == MAX_DIST and maxPickup == MAX_DIST:
            break

        distance = max(maxDelivery, maxPickup) + 1

        answer += distance * 2

    return answer


cap = 4
n = 5
d = [1, 0, 3, 1, 2]
p = [0, 3, 0, 4, 0]

cap1 = 2
n1 = 7
d1 = [1, 0, 2, 0, 1, 0, 2]
p1 = [0, 2, 0, 1, 0, 2, 0]

cap2 = 4
n2 = 3
d2 = [0, 0, 4]
p2 = [0, 4, 0]

print(solution(cap2, n2, d2, p2))
