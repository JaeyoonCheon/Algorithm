"""
    lv.2 2개 이하로 다른 비트
    
    1.  예시로부터의 규칙성을 잘 찾아야 하는 문제.
    2.  짝수인 경우, xxx10으로 끝나므로 xxx11로 만드는 것이 가장 크면서 가까운 수이므로 1을 더한 값을 결과에 추가.
    3.  홀수인 경우, 오른쪽 비트로부터 처음 0이 나오는 위치의 01을 10(+1)으로 대치하는 것이 가장 크면서 가까운 수이다.
"""


def solution(numbers):
    answer = []

    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            toBinary = f"0{bin(number)[2:]}"
            toBinary = f"{toBinary[:toBinary.rindex('0')]}10{toBinary[toBinary.rindex('0')+2:]}"
            answer.append(int(toBinary, 2))

    return answer
