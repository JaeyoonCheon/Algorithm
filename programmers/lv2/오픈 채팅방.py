"""
    lv.2 오픈 채팅방
    
    1.  먼저 동작을 수행해 uuid - name 쌍을 최종까지 변화시킨다.
    2.  이후 기록된 동작들에 대해 출력
"""


def solution(record):
    answer = []

    db = {}
    actions = []

    for action in record:
        action = action.split(" ")
        op, uuid = action[0], action[1]

        if op == "Enter" or op == "Change":
            name = action[2]
            db[uuid] = name
        actions.append(action)

    for log in actions:
        op, uuid = log[0], log[1]

        if op == "Enter":
            answer.append(f"{db[uuid]}님이 들어왔습니다.")
        elif op == "Leave":
            answer.append(f"{db[uuid]}님이 나갔습니다.")

    return answer


solution(
    [
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan",
    ]
)
