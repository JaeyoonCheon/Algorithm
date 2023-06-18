"""
    lv.1 신규 아이디 추천
    
    1.  문자열 변환 메소드를 양지해 놓을것.
"""


def solution(new_id):
    answer = ""

    step1 = new_id.lower()
    step2 = []

    for c in step1:
        if c.isalpha() or c.isdigit() or c in ["-", "_", "."]:
            step2.append(c)
    step2 = "".join(step2)

    while ".." in step2:
        step2 = step2.replace("..", ".")

    step3 = step2

    step4 = step3.strip(".")
    answer = step4

    if answer == "":
        answer = "a"
    elif len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    if len(answer) <= 2:
        last = answer[-1]

        while len(answer) < 3:
            answer += last

    return answer


result = solution("abcdefghijklmn.p")
print(result)
