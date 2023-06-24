"""
    lv.1 키패드 누르기
    
    1.  키패드를 좌표로 하는 구현 문제.
    2.  왼쪽/오른쪽/가운데(우선 손 먼저) 규칙에 따라 구현.
"""


def checkDist(pos, target, hand):
    leftDist = abs(pos["left"][0] - target[0]) + abs(pos["left"][1] - target[1])
    rightDist = abs(pos["right"][0] - target[0]) + abs(pos["right"][1] - target[1])

    if leftDist > rightDist:
        return "right"
    elif leftDist < rightDist:
        return "left"
    else:
        return hand


def solution(numbers, hand):
    answer = ""

    pos = {"left": [3, 0], "right": [3, 2]}
    finger = {"left": [1, 4, 7, "*"], "mid": [2, 5, 8, 0], "right": [3, 6, 9, "#"]}

    for number in numbers:
        if number in finger["left"]:
            answer = answer + "L"
            pos["left"] = [finger["left"].index(number), 0]
        elif number in finger["right"]:
            answer = answer + "R"
            pos["right"] = [finger["right"].index(number), 2]
        else:
            target = [finger["mid"].index(number), 1]

            if checkDist(pos, target, hand) == "left":
                answer = answer + "L"
                pos["left"] = target
            else:
                answer = answer + "R"
                pos["right"] = target

    return answer
