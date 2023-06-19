"""
    lv.2 위장
    
    1.  각 의상 종류 별 선택할 수 있는 경우의 수는 해당 종류 의상 개수 + 1(선택하지 않는 경우)이다.
        모든 종류의 경우의 수를 곱하고, 의상을 입지 않는 경우 1가지는 존재할 수 없으므로 1을 빼준다.
"""


def solution(clothes):
    answer = 1

    category = []
    closet = {}

    for cloth, type in clothes:
        closet[type] = closet.get(type, 0) + 1

    for type in closet:
        answer *= closet[type] + 1

    answer = answer - 1

    return answer


result = solution(
    [
        ["yellow_hat", "headgear"],
        ["blue_sunglasses", "eyewear"],
        ["green_turban", "headgear"],
    ]
)
