"""
    lv.1 이상한 문자 만들기
    
    1.  개별 단어를 공백 인덱스로 초기화하면서 체크.
    2.  단어의 글자 각각을 홀/짝에 따라 변환.
"""


def solution(s):
    wordIdx = 0

    string = list(s)

    for i in range(len(string)):
        c = string[i]

        if c == " ":
            wordIdx = 0
            continue
        elif wordIdx % 2 == 0:
            string[i] = c.upper()
        else:
            string[i] = c.lower()

        wordIdx += 1

    answer = "".join(string)

    return answer
