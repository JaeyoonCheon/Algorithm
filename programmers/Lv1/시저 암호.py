"""
    lv.1 시저 암호
    
    1.  아스키코드 전환 -> 문자 수정 -> 문자열 전환의 과정만 거치면 풀이 가능.
    2.  문자를 대문자/소문자 범위 내에서 전환할 때, 알파벳 26자 내에서 회전하도록 mod 26을 해주는데,
        이 때 대문자/소문자 a를 빼고 계산한 뒤 다시 더해주어야 정상적으로 계산이 된다.
"""


def solution(s, n):
    answer = list(s)

    for i in range(len(answer)):
        c = answer[i]
        if c == " ":
            continue
        elif c.islower():
            answer[i] = chr((ord(c) - ord("a") + n) % 26 + ord("a"))
        else:
            answer[i] = chr((ord(c) - ord("A") + n) % 26 + ord("A"))

    return "".join(answer)


result = solution("AB", 1)

print(result)
